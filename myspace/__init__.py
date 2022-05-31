from flask import Flask, render_template, request, redirect

import database


app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
	# if request.method == "POST":
	# 	user = request.form['login_username']
	# 	pass = request.form['login_password']
	#
	# 	error = ""
	# 	#check if username and password are valid
	# if request.method == "GET":
	# 	if (session.get('username') is not None):
	# 		return redirect("/")
	# 	else:
	# 		return render_template('login.html')
	return render_template('login.html')

@app.route('/register', methods=['GET','POST'])
def register():
	# if request.method == "POST":
	# 	new_user = request.form['register_username']		]
	# 	new_pass = request.form['register_password']
	#
	# 	error = ""
	# 	if not new_user:
	# 		error = "There was no username entered!"
	# 	elif not new_pass:
	# 		error = "There was no password entered!"
	#	#then check if the username is unique
	# if request.method == "GET":
	# 	if (session.get('username') is not None):
	# 		return redirect("/")
	# 	else:
	# 		return render_template('register.html')
	return render_template('register.html')

if __name__ == '__main__':
        database.db_setup()
        app.debug = True
        app.run(host="localhost", debug=True)
