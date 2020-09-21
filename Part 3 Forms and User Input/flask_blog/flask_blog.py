from flask import Flask, render_template, url_for, flash, redirect
from forms import RegForm, LogForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '2a48340099afdaa1b757452ba8d04744'

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
	forms = LogForm()
	if forms.validate_on_submit():
		if forms.email.data == 'jane@doe.com' and forms.password.data == '123456789':
			flash(f'You have been logged in!', 'success')
			return redirect(url_for('home'))
		else:
			flash(f'Login Unsuccesful! Please check your email id and password', 'danger')
	return render_template('login.html', title='Login', form=forms)

@app.route('/register', methods=['POST', 'GET'])
def register():
	forms = RegForm()
	if forms.validate_on_submit():
		flash(f'Account created for { forms.username.data }!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=forms)

if __name__ == '__main__':
	app.run(debug=True)