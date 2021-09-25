from db import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask import session
import routes

def all_courses():
	sql = "SELECT * FROM courses"
	result = db.session.execute(sql)
	all = result.fetchall()
	return all

def add_course(name):
	sql = "INSERT INTO courses (name) VALUES (:name)"
	db.session.execute(sql, {"name":name})
	db.session.commit()

def attending(id, user_id):
	sql = "SELECT * FROM course WHERE user_id=:user_id"
	result = db.session.execute(sql, {"user_id":user_id})
	attending = result.fetchone()
	if not attending:
		return False
	else:
		return True

def attend_course(user_id, course_id):
	sql = "INSERT INTO course (user_id, course_id) VALUES (:user_id, :course_id)"
	db.session.execute(sql, {"user_id":user_id, "course_id":course_id})
	db.session.commit()
