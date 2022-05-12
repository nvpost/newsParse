import requests
from bs4 import BeautifulSoup

import func
import rules
from sql import send_data_sql

common_dateFormat = '%d.%m.%Y'
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.5.769 Yowser/2.5 Safari/537.36"

def main_logic(el):

    print('--------------------------------------')
    print(el['url'])
    group_id = el['category']
    try:
        group_id = ", ".join(el['dop_cat'])
    except:
        pass
    site_id = el['name']
    site_name = el['name']
    url = el['url']
    lang = el['place']
    try:
        _format = el['date_format']
    except:
        _format = common_dateFormat

    try:
        url_prefix = el['url_prefix']
    except:
        url_prefix = ""

    try:
        page = requests.get(el['url'], timeout=(5, 15), headers={'User-Agent': userAgent})
    except:
        print('Не получили', site_id)
        return False

    try:
        page.encoding = el['encoding_']
        # page.encoding = 'UTF-8'
    except:
        pass

    try:
        image_prefix = el['image_url']['image_prefix']
    except:
        image_prefix = ""

    soup = BeautifulSoup(page.text, "html.parser")

    try:
        if el['root_']:
            rootElem = soup.select(el['root_']['selector'])[el['root_']['position']]
            items = rootElem.select(el['items_']['selector'])
        else:
            items = soup.select(el['items_']['selector'])
    except:
        items = soup.select(el['items_']['selector'])
        print("Не получили rootElem для", site_id)

    newsArr = []
    for i in items:
        date = ""
        title = ""
        image_url=""
        link = el['url']

        try:
            title = func.changeSymbol(i.select(el['title_']['selector'])[el['title_']['position']].text)
        except:
            pass
        try:
            if el['link_']:
                link = i.select(el['link_']['selector'])[el['link_']['position']].get('href')
                if (el['name'] == "Atonics"):
                    link = link.replace('javascript:view(', '')
                    link = link.replace(');', '')
        except:
            pass

        try:
            date = func.changeSymbol(i.select(el['date_']['selector'])[el['date_']['position']].text)
            # Исключения для даты
            date = rules.dateRules(el['name'], date, title)
            print(date)
            date = func.cleanDate(date)
        except:
            pass

        image_url = rules.imgRules(el, i, image_prefix)

        if (len(date) > 2):
            date = func.df(date, _format)

        full_link = url_prefix + link

        if link.find('http') == 0:
            full_link = link

        if title != "":
            newsArr.append(
                (site_id, group_id, lang, date, title, full_link, 0, image_url)
            )
            # send_data_sql.updateImg(image_url, title, site_id)



    # print("Всего новостей: ", len(newsArr))

    donor_arr = (site_id, site_name, url, group_id, lang)
    # print(donor_arr)

    send_data_sql.add_data(newsArr, site_id)
    # send_data_sql.add_donor(donor_arr)
    # # print(newsArr)
    #
    print("Всего добавлено новостей", send_data_sql.addCounter)