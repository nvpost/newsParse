import config

db = config.db

cursor = db.cursor()

def add_data(newsArr):

    query = """INSERT INTO products(site_id, group_id, lang, news_date, title, link, status)
    values(%s, %s, %s, %s, %s, %s, %s)"""


    cursor = db.cursor()
    cursor.executemany(query,newsArr)
    db.commit()