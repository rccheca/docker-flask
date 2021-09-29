from re import A
from flask import Blueprint, request, jsonify, abort, Response, redirect, url_for, flash
from flask.templating import render_template
import include.db as db


mod = Blueprint('forms', __name__)


@mod.route('/ok', methods=['GET'])
def ok():
	return "ok"


@mod.route('/create/brand', methods=['GET', 'POST'])
def create_brand():
	form = []
	
	if request.form:
		print(request.form)
		form = request.form
		if form['id']:
			db.insert_db("update brand name=%s where id = %s",args=(form['name'],form['id']))
			return redirect(url_for('blog.brand_list'))
		else:
			name = form['name']
			db.insert_db("insert into brand (name) values (%s)",args=(name,))
			flash(f'The brand <b>{name}</b> has been created correctly!')
			return redirect(url_for('blog.brand_list'))


	if request.form:
		form = request.form
	return render_template('blog/brand_form.html', form= form)

@mod.route('/update/brand/<int:id>', methods=['GET','POST'])
def update_brand(id):

	if request.form and request.form['id']:
		form = request.form
		db.insert_db("update brand set name=%s where id = %s",args=(form['name'],form['id']))
		return redirect(url_for('blog.brand_list'))

	form= db.query_db('select * from brand where id = %s',args=(id,), one=True)

	return render_template('blog/brand_form.html', form= form, edit=True)
	return f"ok {id}"

@mod.route('/delete/brand/<int:id>', methods=['GET','POST'])
def delete_brand(id):
	db.id_or_404('brand',id)
	db.insert_db("delete from brand where id = %s",args=(id,))
	flash('The brand has been deleted correctly!')
	return redirect(url_for('blog.brand_list'))
	return "ok"


@mod.route('/create/car', methods=['GET', 'POST'])
def create_car():
	form = []
	
	if request.form:
		print(request.form)
		form = request.form
		if form['id']:
			db.insert_db("update brand name=%s where id = %s",args=(form['name'],form['id']))
			return redirect(url_for('blog.brand_list'))
		else:
			name = form['name']
			db.insert_db("insert into cars (name,km,comment,brand_id) values (%s,%s,%s,%s)",args=(name,form['km'],form['comments'],form['brand']))
			flash(f'The car <b>{name}</b> has been created correctly!')
			return redirect(url_for('blog.car_list'))


	if request.form:
		form = request.form
	brands= db.query_db('select * from brand')

	return render_template('blog/car_form.html', form= form, brands=brands)

@mod.route('/update/car/<int:id>', methods=['GET','POST'])
def update_car(id):

	if request.form and request.form['id']:
		form = request.form
		db.insert_db("update cars set name=%s, km=%s, comment=%s, brand_id=%s where id = %s",args=(form['name'],form['km'],form['comments'],form['brand'],form['id']))
		flash('The car <b>%s</b> has been updated correctly!'%form['name'])
		return redirect(url_for('blog.car_list'))

	form= db.query_db('select * from cars where id = %s',args=(id,), one=True)

	brands= db.query_db('select * from brand')

	print(brands)

	return render_template('blog/car_form.html', form= form, brands = brands, edit=True)
	return f"ok {id}"

@mod.route('/delete/car/<int:id>', methods=['GET','POST'])
def delete_car(id):
	db.id_or_404('cars',id)
	db.insert_db("delete from cars where id = %s",args=(id,))
	flash('The car has been deleted correctly!')
	return redirect(url_for('blog.car_list'))
	return "ok"