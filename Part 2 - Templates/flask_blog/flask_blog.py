from flask import Flask, render_template

app = Flask(__name__)


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

if __name__ == '__main__':
	app.run(debug=True)