# flaskblog
Contents and code for the COURSE

# This is for reference for the Introduction to Backend using Python and Flask

## 1. Creating the FIRST FLASK APP
	In any desired folder create a python file(py)
	The contents of the file should be
	
	from flask import Flask
	app = Flask(__name__)
	@app.route('/')
	def hello():
		return "Hello World"
	

## 2. Running the Flask app example.py
	There are 2 methods to run the application
	a. Use the Flask variables from the command prompt or terminal
	   *For Windows:
		set FLASK_APP=example.py
		set FLASK_DEBUG=1
	   * For Linux and Mac
		export FLASK_APP=example.py
		export FLASK_DEBUG=1
	b. Run the python file directly from the TERMINAL
	   *To achieve the following, the following code snippet must be inserted in the example.py file
	
	   if __name__ == '__main__':
	   	app.run(debug=True)
	
	   After the following code has been inserted then in the terminal enter the following command
	   $python example.py
