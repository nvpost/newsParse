from bs4 import BeautifulSoup
import requests
import datetime
import func

from sql import send_data_sql
from data import kip_ru

userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.5.769 Yowser/2.5 Safari/537.36"

common_dateFormat = '%d.%m.%Y'
for el in kip_ru.data:
    print('--------------------------------------')
    print(el['url'])

    group_id = el['category']
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

    lang = el['place']

    page = requests.get(el['url'], timeout=(5, 15), headers={'User-Agent': userAgent})
    page.encoding = 'UTF-8'
    soup = BeautifulSoup(page.text, "html.parser")

    rootElem = soup.select(el['root_']['selector'])[el['root_']['position']]

    items = rootElem.select(el['items_']['selector'])
    newsArr = []
    for i in items:
        date = ""
        title = ""
        link = el['url']

        try:
            date = func.changeSymbol(i.select(el['date_']['selector'])[el['date_']['position']].text)
        except:
            pass
            # print("Не удалось получить дату")
        try:
            title = func.changeSymbol(i.select(el['title_']['selector'])[el['title_']['position']].text)
        except:
            pass
            # print("Не удалось получить Название")
        try:
            if el['link_']:
                link = i.select(el['link_']['selector'])[el['link_']['position']].get('href')
                if (el['name'] == "Atonics"):
                    link = link.replace('javascript:view(', '')
                    link = link.replace(');', '')
        except:
            pass
            # print("Не удалось получить ссылку")

        date = func.df(date, _format)
        # try:
        #     date = func.df(date, format)
        # except:
        #     pass
        #     # print("Не удалось установить")

        link = url_prefix + link

        if title != "":
            newsArr.append(
                (site_id, group_id, lang, date, title, link, 0)
            )


            print(date)
            print(title)
            print(link)
    print("Всего новостей: ", len(newsArr))

    donor_arr = (site_id, site_name, url, group_id, lang)
    print(donor_arr)
    # print(newsArr)
    send_data_sql.add_data(newsArr)
    # send_data_sql.add_donor(donor_arr)











