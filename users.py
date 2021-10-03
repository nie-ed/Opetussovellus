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
			return user.id
		else:
			return False

def create_user(username, hash_value):
	sql = "INSERT INTO users (username, password, admin) VALUES (:username, :password, :admin)"
	db.session.execute(sql, {"username":username, "password":hash_value, "admin":False})
	db.session.commit()	
	sql = "SELECT id FROM users WHERE username=:username"
	result = db.session.execute(sql, {"username":username})
	user = result.fetchone()
	if not user:
		return False
	else:
		return True
		
def is_admin(user_id):
	sql = "SELECT * FROM users WHERE id=:id"
	result = db.session.execute(sql, {"id":user_id})
	user = result.fetchone()
	return user.admin

def is_user(user_id):
	sql= "SELECT * FROM users WHERE id=:id"
	result = db.session.execute(sql, {"id":user_id})
	user = result.fetchone()
	if user:
		return True
	else:
		return False

def user_id(user_id):
	sql= "SELECT id FROM users WHERE id=:id"
	result = db.session.execute(sql, {"id":user_id})
	id_user = result.fetchone()
	return id_user
