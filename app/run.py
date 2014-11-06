from flask import *
import sqlite3


app = Flask(__name__)
@app.route('/')
def home():
	return render_template('home2.html')

@app.route('/<filename>',methods=['POST'])
def save(filename=None):
	conn=sqlite3.connect('paint.db')
	c=conn.cursor()
	c.execute("INSERT INTO paintstore (title,imagedata) VALUES (?,?)",[request.form['name'],request.form['data']])
	conn.commit()
	conn.close()
	return render_template('home2.html')
@app.route('/gallery')
def gallery():
	conn=sqlite3.connect('paint.db')
	c=conn.cursor()
	c.execute("SELECT * FROM paintstore ORDER BY id desc")
	posts=[dict(id=i[0],title=i[1]) for i in c.fetchall()]
	conn.commit()
	conn.close()	
	return render_template('gallery.html',posts=posts)
@app.route('/gallery/<filename>',methods=['GET'])
def load(filename=None):
	conn=sqlite3.connect('paint.db')
	c=conn.cursor()	
	c.execute("SELECT * FROM paintstore WHERE title=?",[filename])
	posts=[dict(id=i[0],title=i[1],imagedata=i[2]) for i in c.fetchall()]
	return render_template('picload.html',posts=posts)


app.run(debug = True)




