import sqlite3
conn = sqlite3.connect('paint.db') 
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS paintstore")
c.execute('''CREATE TABLE paintstore(id serial,title text,imagedata text)''')
conn.commit()
conn.close()
