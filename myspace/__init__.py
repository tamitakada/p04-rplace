from flask import Flask, render_template, request
import database


app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/register')
def register():
	return render_template('register.html')

if __name__ == '__main__':
        database.db_setup()
        app.debug = True
        app.run(host="localhost", debug=True)
