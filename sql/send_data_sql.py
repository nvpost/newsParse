import pymysql


db = pymysql.connect(host="localhost",
                      user='root',
                      password='',
                      database='news_site',
                      charset='utf8mb4')

# db = config.db

cursor = db.cursor()

def add_data(newsArr):

    query = """INSERT INTO news(site_id, group_id, lang, news_date, title, link, status)
    values(%s, %s, %s, %s, %s, %s, %s)"""

    cursor.executemany(query,newsArr)
    db.commit()

def add_donor(donorArr):
    query = """INSERT INTO news_donor(site_id, name, link, category, lang)
    values(%s, %s, %s, %s, %s)"""


    cursor.execute(query,donorArr)
    db.commit()