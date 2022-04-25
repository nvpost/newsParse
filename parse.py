from bs4 import BeautifulSoup
import requests
import datetime
import func

from sql import send_data_sql



from data import sp_ru
from data import mt
from data import sensors
from data import op_ru
from data import kip
from data import p4v_ru
from data import pr
from data import agregator


userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.5.769 Yowser/2.5 Safari/537.36"
addCounter = 0

an_chunks = [
    op_ru.data,
    pr.data,
    kip.data,
    sp_ru.data,
    p4v_ru.data,
    sensors.data,
    mt.data,
    agregator.data
]
allData = []
for i in an_chunks:
    allData = allData + i

common_dateFormat = '%d.%m.%Y'

for el in agregator.data:
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
        continue

    try:
        page.encoding = el['encoding_']
        # page.encoding = 'UTF-8'
    except:
        pass

    soup = BeautifulSoup(page.text, "html.parser")

    if el['root_']:
        rootElem = soup.select(el['root_']['selector'])[el['root_']['position']]
        items = rootElem.select(el['items_']['selector'])
    else:
        items = soup.select(el['items_']['selector'])


    newsArr = []
    for i in items:
        date = ""
        title = ""
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
            if (el['name'] == "Atonics"):
                date = date.split(' ')[0]
            if el['name'] == "ООО «Стэнли» (Корунд)":
                date = date.split(' ')[0]
            if el['name'] == "Теплоприбор Челябинск":
                date = date.split(' ')[0]
            if el['name'] == 'Провенто':
                date = date + '.2022'
            if el['name'] == 'TDM ELECTRIC':
                date = date.replace('—', '2022')

            if (el['name'] == "Е_Е"):
                month_list = ['January', 'February', 'March', 'April', 'May', 'June',
                              'July', 'August', 'September', 'October', 'November', 'December']
                for m in range(len(month_list)):
                    old = month_list[m]
                    date = date.replace(old, str(m + 1) + '.')

            date = func.cleanDate(date)
        except:
            pass

# Исключения
        if (el['name'] == "Endress"):
            date = title.split(' ')[0]
            print(date)
        # Исключения


        if (len(date) > 2):
            date = func.df(date, _format)

        full_link = url_prefix + link

        if link.find('http')==0:
            full_link = link



        if title != "":
            newsArr.append(
                (site_id, group_id, lang, date, title, full_link, 0)
            )


    # print("Всего новостей: ", len(newsArr))

    donor_arr = (site_id, site_name, url, group_id, lang)
    # print(donor_arr)

    send_data_sql.add_data(newsArr, site_id)
    send_data_sql.add_donor(donor_arr)
    # # print(newsArr)
    #
    print("Всего добавлено новостей", send_data_sql.addCounter)












