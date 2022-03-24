from bs4 import BeautifulSoup
import requests
import sqlite3

from data import kip_ru


connection = sqlite3.connect('News.db')
cursor = connection.cursor()

userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.5.769 Yowser/2.5 Safari/537.36"

# el = base.kip
for el in kip_ru.data:
    print('--------------------------------------')
    print(el['url'])

    page = requests.get(el['url'], timeout=10, headers={'User-Agent': userAgent})
    soup = BeautifulSoup(page.text, "html.parser")

    rootElem = soup.select(el['root_']['selector'])[el['root_']['position']]

    items = soup.select(el['items_']['selector'])
    insertData = []
    for i in items:
        date = ""
        title = ""
        link = ""

        date = i.select(el['date_']['selector'])[el['date_']['position']].text
        title = i.select(el['title_']['selector'])[el['title_']['position']].text
        if el['link_']:
            link = i.select(el['link_']['selector'])[el['link_']['position']].get('href')


        insertData.append([1, date, title, link, 0])

    print(insertData)






# def addToBase(records):
#     sql_query = """INSERT INTO News
#                 (firm_id, news_date, label, text, status)
#                 VALUES (?, ?, ?, ?, ?)"""
#     cursor.executemany(sql_query, records)
#     connection.commit()


# addToBase(insertData)



