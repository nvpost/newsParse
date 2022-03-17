from bs4 import BeautifulSoup
import requests

from data import base


el = base.kip[0]
page = requests.get(el['url'])

soup = BeautifulSoup(page.text, "html.parser")


rootElem = soup.select(el['root_']['selector'])[el['root_']['position']]


items = soup.select(el['items_']['selector'])

for i in items:
    date = i.select(el['date_']['selector'])[el['date_']['position']].text
    title = i.select(el['title_']['selector'])[el['title_']['position']].text
    link = i.select(el['link_']['selector'])[el['link_']['position']].get('href')

    print(date)
    print(title)
    print(link)



