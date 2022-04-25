import pymysql


db = pymysql.connect(host="localhost",
                      user='root',
                      password='',
                      database='news_site',
                      charset='utf8mb4',
                      cursorclass=pymysql.cursors.DictCursor)

# db = config.db

cursor = db.cursor()
# id = 2348
# cursor.execute("SELECT * FROM news WHERE link LIKE '%soel.ru%'")
cursor.execute("SELECT * FROM news WHERE id = 2348")

now_have = cursor.fetchall()


repair_arr = []

a = ('a', 'f', '4')
for row in now_have:
    for i in row:
        v = row[i]
        if i == 'link':
            v = 'new_value_'+v
        repair_arr.append(v)
print(repair_arr)



# query = """IUPDATE news(id, site_id, group_id, lang, news_date, title, link, status, parse_date)
# values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"""


update_qwe = """UPDATE news (SELECT id, parse_date FROM news) SET link = REPLACE(link, 'soel.ru//', 'soel.ru/'), parse_date = news.parse_date WHERE id = news.id"""

cursor.execute(update_qwe)

# id
# site_id
# group_id
# lang
# news_date
# title
# link
# status
# parse_date




