from bs4 import BeautifulSoup
import requests
import datetime



# from data import sp_ru
# from data import op_ru


from data import sp_ru
from data import p4v_ru

from data import agregator

import func_old


# from data import sensors
from data_imgs import pr
from data_imgs import kip
from data_imgs import mt



from sql import send_data_sql

# an_chunks = [
#     op_ru.data,
#     pr.data,
#     kip.data,
#     sp_ru.data,
#     p4v_ru.data,
#     sensors.data,
#     mt.data
# ]
# allData = []
# for i in an_chunks:
#     allData = allData + i


userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.5.769 Yowser/2.5 Safari/537.36"

common_dateFormat = '%d.%m.%Y'

el = pr.data[5]
group_id = el['category']
# меняем id на имя
site_id = el['name']
site_name = el['name']
url = el['url']
lang = el['place']
dateFormatFlag = False

try:
    format = el['date_format']
    dateFormatFlag = True
except:
    format = common_dateFormat


try:
    url_prefix = el['url_prefix']
except:
    url_prefix = ""

try:
    image_prefix = el['image_url']['image_prefix']
except:
    image_prefix = ""

page = requests.get(el['url'], timeout=(5, 15), headers={'User-Agent': userAgent})

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
link = el['url']
for i in items:
    date = ""
    title = ""



    try:
        title = func.changeSymbol(i.select(el['title_']['selector'])[el['title_']['position']].text)

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

        if(el['name']=="Automation World Products") or (el['name']=="999automation"):
            date = date.replace('th', '.', 1)
            date = date.replace('nd', '.', 1)
            date = date.replace('st', '.', 1)
        if(el['name']=="КИПиС") or (el['name']=="Automate"):
            date = date.split('|')[0]
        if(el['name']=="Manufacturing Tomorrow"):
            date = date.split(':')[0]

        if (el['name'] == "Е_Е"):
            month_list = ['January', 'February', 'March', 'April', 'May', 'June',
                                'July', 'August', 'September', 'October', 'November', 'December']
            for m in range(len(month_list)):
                old = month_list[m]
                date = date.replace(old, str(m + 1) + '.')

        if 'Elec ' in el['name']:
            today = 'Сегодня'
            est_day = 'Вчера'
            if today in date:
                date = str(datetime.datetime.today())
                date = date.split(' ')[0]
                date = date.split('-')
                date = date[2] + '.' + date[1] + '.'  + date[0]
            elif est_day in date:
                date = str(datetime.datetime.today() - datetime.timedelta(days=1))
                date = date.split(' ')[0]
                date = date.split('-')
                date = date[2] + '.' + date[1] + '.'  + date[0]
            else:
                date = date.split('в')[0]


        # print(date)
        # print(format)
        # print(el['name'])
        date = func.cleanDate(date)
    except:
        pass


    try:
        if el['link_']:

            # print(i.select(el['link_']['selector'])[el['link_']['position']].get('href'))
            if(el['name']=="Atonics"):
                link = link.replace('javascript:view(', '')
                link = link.replace(');', '')

            if el['link_']['selector']=='_self_item_':
                    link = i.get('href')
            else:
                link = i.select(el['link_']['selector'])[el['link_']['position']].get('href')
    except:
        pass


    if el['name'] == "Endress":
        date = title.split(' ')[0]



    # if el['name'] == "Yokogawa":
    #     d = i.select('.date')
    #     if d != []:
    #         date = d[0].text
    #         date = func.cleanDate(date)

    try:
        if 'Phoenix contact' in el['name'] or 'APLISENS' in el['name'] or 'Теплоприбор Челябинск' in el['name'] or 'Schneider Electric' in el['name'] or 'Automate' in el['name'] or 'Werma' in el['name'] or 'teremonline.ru' in el['name']:
            image_url = (i.select(el['image_url']['selector'])[el['image_url']['position']].get('style')).strip()
            image_url = image_url.replace(el['image_url']['replace_before'], '')
            image_url = image_url.replace(el['image_url']['replace_after'], '')
        elif 'Вектор ВС' in el['name']:
            image_url = (i.select(el['image_url']['selector'])[el['image_url']['position']].get('data-bg-src'))
        elif 'Полтраф СНГ' in el['name'] or 'Кип-сервис' in el['name'] or 'Werma' in el['name']:
            image_url = (i.select(el['image_url']['selector'])[el['image_url']['position']].get('data_1-src'))
        elif 'Werma' in el['name'] or 'РИЗУР' in el['name'] or 'Aereco' in el['name']:
            image_url = (i.select(el['image_url']['selector'])[el['image_url']['position']].get('data-src'))
        else:
            image_url = (i.select(el['image_url']['selector'])[el['image_url']['position']].get('src'))
        image_url = image_prefix + image_url
    except:
        image_url = 'нет изображения'



    if (len(date)>2):

        # print('--main date--')
        # print(date)
        # print('--main date--')
        date = func.df(date, format)


    if title != "":
        newsArr.append(
            (site_id, group_id, 'ru', date, title, link, 0)
        )
        link = url_prefix+link


        print(title)
        print(link)
        print(date)
        print(image_url)
        print("-------------------------------------------------------------------------")
print("-------------------------------------------------------------------------")
print("Всего новостей: ", len(newsArr))
# print(site_id)

donor_arr=(site_id, site_name, url, group_id, lang)

print(donor_arr)



# send_data_sql.add_data(newsArr, site_id)
# send_data_sql.add_donor(donor_arr)