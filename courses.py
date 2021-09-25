from db import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask import session

def all_courses():
	sql = "SELECT * FROM courses"
	result = db.session.execute(sql)
	all = result.fetchall()
	return all

def add_cource(name):
	sql = "INSERT INTO courses (name) VALUES (:name)"
	db.session.execute(sql, {"name":name})
	db.session.commit()

