from db import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask import session

def get_user(username, password):
	sql = "SELECT id, password FROM users WHERE username=:username"
	result = db.session.execute(sql, {"username":username})
	user = result.fetchone()
	if not user:
		return False
	else:
		hash_value = user.password
		if check_password_hash(hash_value, password):
			session["user_id"] = user.id
			return user.id
		else:
			return False

def create_user(username, hash_value):
	sql = "INSERT INTO users (username, password, admin) VALUES (:username, :password, :admin)"
	db.session.execute(sql, {"username":username, "password":hash_value, "admin":True})
	db.session.commit()	
	sql = "SELECT id FROM users WHERE username=:username"
	result = db.session.execute(sql, {"username":username})
	user = result.fetchone()
	if not user:
		return False
	else:
		return True
		
def is_admin(id):
	sql = "SELECT admin FROM users WHERE id=:id"
	result = db.session.execute(sql, {"id":id})
	admin = result.fetchone()
	if admin:
		return True
	else:
		return False

def is_user():
	sql= "SELECT * FROM users WHERE username=:username"
	result = db.session.execute(sql, {"username":session["username"]})
	user = result.fetchone()
	if user:
		return True
	else:
		return False

def user_id():
	sql= "SELECT id FROM users WHERE username=:username"
	result = db.session.execute(sql, {"username":session["username"]})
	id_user = result.fetchone()
	return id_user
