from flask import Flask
from flask import g
import os
from flask.templating import render_template
import mysql.connector
import blog


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['EXPLAIN_TEMPLATE_LOADING'] = True
app.secret_key = 'c308caf65e461a225f4d'

def get_db():
	db = getattr(g, '_database', None)
	MYSQL_ROOT_PASSWORD = os.environ.get("MYSQL_ROOT_PASSWORD")
	if db is None:
		import mysql.connector
		db = g._database = mysql.connector.connect(user='root', password=MYSQL_ROOT_PASSWORD,
								host='mysql',
								database='app',
								use_pure=True)
	# def make_dicts(cursor, row):
	# 	return dict((cursor.description[idx][0], value)
	# 				for idx, value in enumerate(row))

	# db.row_factory = make_dicts

	return db

def query_db(query, args=(), one=False):
	cur = get_db().cursor(dictionary=True)
	cur.execute(query, args)
	rv = cur.fetchall()
	cur.close()
	return (rv[0] if rv else None) if one else rv



def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.teardown_appcontext
def close_connection(exception):
	db = getattr(g, '_database', None)
	if db is not None:
		db.close()



@app.route("/")
def hello():
	db=get_db()
	for post in query_db('select * from blog'):
		print(post['title'], 'has the id', post['text'])
	print(app.url_map)
	return render_template('index.html')


@app.route("/db")
def db_test():
	MYSQL_ROOT_PASSWORD = os.environ.get("MYSQL_ROOT_PASSWORD")
	db = mysql.connector.connect(user='root', password=MYSQL_ROOT_PASSWORD,
								host='mysql',
								database='app',
								use_pure=True)
	cursor = db.cursor()
	# cursor.execute('select * from blog')
	# rows = cursor.fetchall()
	# print(rows)
	insert=("insert into brand (name) "
	"values (%s)")
	data=('pepe',)

	cursor.execute(insert, data)

	

	return "guay"




app.register_blueprint(blog.mod)