from threading import Lock
from os import urandom

from flask import Flask, render_template, request, redirect, session
from flask_socketio import SocketIO, emit, disconnect

import database


app = Flask(__name__)
app.secret_key = urandom(32)
socketio = SocketIO(app, async_mode=None)
thread = None
thread_lock = Lock()


def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        socketio.sleep(10)
        count += 1
        socketio.emit('my_response',
                      {'data': 'Server generated event', 'count': count})

@socketio.event
def my_broadcast_event(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my_response',
         {'data': message['data'], 'count': session['receive_count']},
         broadcast=True)

@socketio.event
def my_ping():
    emit('my_pong')


@socketio.event
def connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)
    emit('my_response', {'data': 'Connected', 'count': 0})

@app.route('/')
def index():
	pixels = database.get_all_pixels()
	return render_template('index.html', pixels=pixels)

@app.route('/edit', methods=['GET','POST'])
def edit():
	if session.get('username'):
		if request.method == "POST":
			pixelStr = request.form['broadcast_data']
			pixelItems = pixelStr.split(', ')
			x = pixelItems[0]
			y = pixelItems[1]
			color = pixelItems[2]
			database.upsert_pixel(int(x), int(y), color)
		pixels = database.get_all_pixels()
		return render_template('edit.html', pixels=pixels)
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
		if loggedin(): return redirect("/")
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
		if loggedin():
			return redirect("/")
		else: return render_template('register.html')
	return render_template('register.html')

def loggedin():
	return 'username' in session.keys()

if __name__ == '__main__':
        database.db_setup()
        app.debug = True
        socketio.run(app, port=8000)
