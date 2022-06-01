from os import urandom

from flask import Flask, render_template, request, redirect, session
import database


app = Flask(__name__)
app.secret_key = urandom(32)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/edit')
def edit():
	if session.get('username'): return render_template('edit.html')
	else: return redirect('/login')

@app.route('/login', methods=['GET','POST'])
def login():
	if request.method == "POST":
		user = request.form['login_username']
		password = request.form['login_password']
		error = database.attempt_login(user, password)
		if error == 2:
			session['username'] = user 
			return redirect("/")
		elif error == 1: 
			return render_template('login.html', error="Wrong password")
		else:
			return render_template('login.html', error="No user with that username found")
	elif request.method == "GET":
		if (session.get('username') is not None): return redirect("/")
		else: return render_template('login.html')

@app.route('/register', methods=['GET','POST'])
def register():
	if request.method == "POST":
		new_user = request.form['register_username']
		new_pass = request.form['register_password']
		error = ""
		if not new_user: error = "There was no username entered!"
		elif not new_pass: error = "There was no password entered!"
	 	
		if database.attempt_add_user(new_user, new_pass) == 1:
			session['username'] = new_user
			return redirect("/")
		else: error = "Username is not unique"
		
		return render_template('register.html', error=error)
	elif request.method == "GET":
		if (session.get('username') is not None):
			return redirect("/")
		else: return render_template('register.html')
	return render_template('register.html')

if __name__ == '__main__':
        database.db_setup()
        app.debug = True
        app.run(host="localhost", debug=True)
