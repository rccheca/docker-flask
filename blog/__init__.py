from flask import Blueprint, request, jsonify, abort, Response, render_template
import include.db as db


from blog.views import forms

mod = Blueprint('blog', __name__, url_prefix='/blog')
mod.register_blueprint(forms.mod)


@mod.route("/")
def hello2():
	return render_template('index.html')


@mod.route("/brands/")
def brand_list():
	brands= db.query_db('select * from brand')
	print(brands)
	return render_template('blog/brand_list.html', brand_list = brands)

@mod.route("/cars/")
def car_list():
	cars= db.query_db('select c.*, b.name as brand  from cars c left join brand b on c.brand_id = b.id ')
	brand_count = db.query_db('select count(*) as count from brand',one=True)
	print(brand_count)

	return render_template('blog/car_list.html', car_list = cars, brand_count=brand_count['count'])


@mod.route("/test/")
def test_modal():
	return render_template('blog/test_modal.html')



@mod.route("/wtp/")
def wtf():
	from flask_wtf import FlaskForm
	from wtforms import StringField
	from wtforms.validators import DataRequired
	
	class MyForm(FlaskForm):
		name = StringField('name', validators=[DataRequired()])
	
	form =MyForm()


	return render_template('index.html', form=form)
