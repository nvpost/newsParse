import sqlite3

connection = sqlite3.connect('News.db')
cursor = connection.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS News
              (id INTEGER PRIMARY KEY, 
              firm_id INT, 
              news_date TEXT,
              label TEXT,
              text TEXT,
              status INT,
              parse_date DATETIME
              )''')