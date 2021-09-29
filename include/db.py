from flask import g, abort
import os


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


def insert_db(query, args=()):
	cur =  get_db().cursor()
	cur.execute(query, args)
	id = cur.lastrowid
	get_db().commit()
	cur.close()
	return id

def id_or_404(table, id):
	cur =  get_db().cursor()
	cur.execute('select count(1) from %s where id = %s'%(table,id))
	re = cur.fetchone()
	if re[0] is 0:
		abort(404)