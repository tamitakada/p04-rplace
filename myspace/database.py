import sqlite3
import random
import os
import hashlib


def get_db():
    return sqlite3.connect("database.db")


def db_setup():
    db = get_db()
    c = db.cursor()

    command = """CREATE TABLE IF NOT EXISTS users (
        id         		INTEGER PRIMARY KEY,
        username     		TEXT,
        password 		VARBINARY,
        salt			BINARY,
        last_contribution 	DATETIME
        );"""
    c.execute(command)
    
    command = """CREATE TABLE IF NOT EXISTS canvas (
        id	INTEGER PRIMARY KEY,
        x     	INTEGER KEY,
        y 	INTEGER KEY,
        color	TEXT
    );"""
    c.execute(command)

    db.commit()
    db.close()


# table param should be "users" or "canvas"
def generate_unique_id(table: str):
    db = get_db()
    c = db.cursor()

    item_id = 0
    items = True
    while items:
        item_id = random.randint(1000, 9999)
        command = f"SELECT * FROM {table} WHERE id = ?"
        items = c.execute(command, (item_id,)).fetchone()

    db.close()
    return item_id


"""
    Returns:
        0 - Failed to add user (non unique username)
        1 - Add user success
"""
def attempt_add_user(username: str, password: str):
    db = get_db()
    c = db.cursor()
    
    if find_user_by_username(username): return 0

    user_id = generate_unique_id("users")
    salt = os.urandom(32)
    
    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100000
    )

    command = "INSERT INTO users (id, username, password, salt) VALUES (?, ?, ?, ?)"
    c.execute(command, (user_id, username, key, salt))

    db.commit()
    db.close()
    
    return 1


"""
    Returns:
	0 - No user with that username found
	1 - User found but wrong password
	2 - Successful login
"""
def attempt_login(username: str, password: str):
    user = find_user_by_username(username)
    if user:
        salt = user[3]
        key = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt,
            100000
        )
        if key == user[2]: return 2
        else: return 1
    return 0


def find_user_by_username(username: str):
    db = get_db()
    c = db.cursor()

    command = "SELECT * FROM users WHERE username = ?"
    user = c.execute(command, (username,)).fetchone()

    db.close()

    return user
    
def upsert_pixel(x: int, y: int, color: str):
    db = get_db()
    c = db.cursor()
    
    pixel = find_pixel_from_coordinates(x, y)
    if pixel:
    	command = "UPDATE canvas SET x = ?, y = ?, color = ? WHERE id = ?"
    	c.execute(command, (x, y, color, pixel[0]))
    else: 
    	pixel_id = generate_unique_id("canvas")
    	command = "INSERT INTO canvas (id, x, y, color) VALUES (?, ?, ?, ?)"
    	c.execute(command, (pixel_id, x, y, color,))

    db.commit()
    db.close()
    
def find_pixel_from_coordinates(x: int, y: int):
    db = get_db()
    c = db.cursor()

    command = "SELECT * FROM canvas WHERE x = ? AND y = ?"
    pixel = c.execute(command, (x, y)).fetchone()

    db.close()

    return pixel
