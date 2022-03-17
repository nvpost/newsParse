from bs4 import BeautifulSoup

import requests

url = "https://www.contravt.ru/news-KontrAvt"
root_selector = "table.cell_standart_icon"
items_selector = 'td.cell_standart_icon_text'

date_selector = "span.date_standart.date"
title_selector = "a.menuchilds"
link_selector = "a.short.detail"

page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

rootElem = soup.select_one(root_selector)


items = soup.select(items_selector)

for i in items:
    date = i.select_one(date_selector).text
    title = i.select(title_selector)[1].text
    link = i.select_one(link_selector).get('href')

    print(date)
    print(title)
    print(link)



