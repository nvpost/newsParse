from bs4 import BeautifulSoup
import requests

from data import base

# url = "https://www.contravt.ru/news-KontrAvt"
# root_selector = "table.cell_standart_icon"
# items_selector = 'td.cell_standart_icon_text'
#
# date_selector = "span.date_standart.date"
# title_selector = "a.menuchilds"
# link_selector = "a.short.detail"


el = base.kip[0]
page = requests.get(el['url'])

soup = BeautifulSoup(page.text, "html.parser")


rootElem = soup.select(el['root_selector']['selector'])[el['root_selector']['position']]


items = soup.select(el['items_selector']['selector'])

for i in items:
    date = i.select(el['date_selector']['selector'])[el['date_selector']['position']].text
    title = i.select(el['title_selector']['selector'])[el['title_selector']['position']].text
    link = i.select(el['link_selector']['selector'])[el['link_selector']['position']].get('href')

    print(date)
    print(title)
    print(link)



