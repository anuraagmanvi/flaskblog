import os
import secrets
from PIL import Image
from flask import Flask, render_template, url_for, flash, redirect, request
from flask_blog_pkg import app, bcrypt, db
from flask_blog_pkg.forms import RegForm, LogForm, UpdateAccountForm
from flask_blog_pkg.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

all_posts = [
	{
		'title':'Welcome To Backend',
		'author':'Anuraag Manvi',
		'content':'Hey Guys, I take great pleasure in welcoming you all to this course',
		'date_posted':'Sept. 20 Sun'
	},
	{
		'title':'Good Job',
		'author':'Arindam',
		'content':'Hey Guys, I congratulate all of you for completing the Frontend with flying colours',
		'date_posted':'Sept. 18 Fri'
	},
	{
		'title':'Welcome To Smart Desert Academy',
		'author':'Reddy Eshwar',
		'content':'Hey Guys, I welcome you all to The Smart Desert Academy',
		'date_posted':'Sept. 2 Wed'
	}
]


@app.route('/home')
@app.route('/')
def home():
	return render_template('home.html', title="Home", posts=all_posts)

@app.route('/about')
def about():
	return render_template('about.html', title="About")

@app.route('/login', methods=['POST', 'GET'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	forms = LogForm()
	if forms.validate_on_submit():
		user = User.query.filter_by(email=forms.email.data).first()
		if user and bcrypt.check_password_hash(user.password, forms.password.data):
			login_user(user, remember=forms.remember.data)
			next_page = request.args.get('next')
			flash(f'You have been logged in!', 'success')
			return redirect(next_page) if next_page else redirect(url_for('home'))
		else:
			flash(f'Login Unsuccesful! Please check your email id and password', 'danger')
	return render_template('login.html', title='Login', form=forms)



@app.route('/register', methods=['POST', 'GET'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	forms = RegForm()
	if forms.validate_on_submit():
		hashed_pass = bcrypt.generate_password_hash(forms.password.data).decode('utf-8')
		user = User(username=forms.username.data, email=forms.email.data, password=hashed_pass)
		db.session.add(user)
		db.session.commit()
		flash(f'Account created for { forms.username.data }! Please LOGIN to continue', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=forms)


@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('home'))


def save_dp(image_select):
	ran = secrets.token_hex(8)
	_, fext = os.path.splitext(image_select.filename)
	f_name = current_user.username + ran + fext
	dp_path = os.path.join(app.root_path, 'static/profile_pics', f_name)
	
	out_size = (256, 256)
	i = Image.open(image_select)
	i.thumbnail(out_size)

	i.save(dp_path)
	return f_name


@app.route('/account', methods=['POST', 'GET'])
@login_required
def account():
	form = UpdateAccountForm()
	if form.validate_on_submit():
		if form.dp.data:
			pic_file = save_dp(form.dp.data)
			current_user.img_file = pic_file
		current_user.username = form.username.data
		current_user.email = form.email.data
		db.session.commit()
		flash('Your Account has been updated', 'success')
		return redirect(url_for('account'))
	elif request.method == 'GET':
		form.username.data = current_user.username
		form.email.data = current_user.email
	image_file = url_for('static', filename='profile_pics/' + current_user.img_file)
	return render_template('account.html', title=' MyAccount', image_file=image_file, form=form)