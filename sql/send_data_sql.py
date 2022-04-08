import pymysql


db = pymysql.connect(host="localhost",
                      user='root',
                      password='',
                      database='news_site',
                      charset='utf8mb4',
                      cursorclass=pymysql.cursors.DictCursor)

# db = config.db

cursor = db.cursor()

addCounter = 0

def add_data(newsArr, site_id):
    global addCounter
    query = """INSERT INTO news(site_id, group_id, lang, news_date, title, link, status)
    values(%s, %s, %s, %s, %s, %s, %s)"""



    cursor.execute("SELECT * FROM news WHERE site_id=%s", site_id)

    now_have = cursor.fetchall()

    dataToAdd = []
    for i in newsArr:
        # print(i)
        addFlag = True
        for j in now_have:
            if i[4]==j['title']:
                addFlag = False

        if addFlag:
            print('добавляем ', i[4])
            dataToAdd.append(i)
        # else:
        #     print('недобавляем')



    addCounter = addCounter + len(dataToAdd)
    if(len(dataToAdd)>0):
        print(dataToAdd)
        cursor.executemany(query, dataToAdd)
        db.commit()

def add_donor(donorArr):
    query = """INSERT INTO news_donor(site_id, name, link, category, lang)
    values(%s, %s, %s, %s, %s)"""

    name = donorArr[1]
    cursor.execute("SELECT * FROM news_donor WHERE name=%s", name)
    now_have = cursor.fetchall()
    print(now_have)
    if(len(now_have)==0):
        print('добавили', name)
        cursor.execute(query, donorArr)
        db.commit()



