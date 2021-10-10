from db import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask import session
import routes

def all_courses():
	sql = "SELECT * FROM courses"
	result = db.session.execute(sql)
	all = result.fetchall()
	return all

def get_course(course_id):
	sql = "SELECT * FROM courses WHERE id=:id"
	result = db.session.execute(sql, {"id":course_id})
	course = result.fetchone()
	return course

def add_course(name):
	sql = "INSERT INTO courses (name) VALUES (:name)"
	db.session.execute(sql, {"name":name})
	db.session.commit()
	sql_2 = "SELECT * FROM courses WHERE name=:name"
	result = db.session.execute(sql_2, {"name":name})
	course = result.fetchone()
	sql_3= "INSERT INTO students_in_course (course_id) VALUES (:course_id)"
	db.session.execute(sql_3, {"course_id":course.id})
	db.session.commit()

def attending(id, user_id):
	sql = "SELECT * FROM students_in_course WHERE course_id=:course_id AND user_id=:user_id"
	result = db.session.execute(sql, {"course_id":id, "user_id":user_id})
	attending = result.fetchone()
	if not attending:
		return False
	else:
		return True

def attend_course(id, user_id):
	sql = "INSERT INTO students_in_course (user_id, course_id) VALUES (:user_id, :course_id)"
	db.session.execute(sql, {"user_id":user_id, "course_id":id})
	db.session.commit()

def user_attends(user_id):
	sql = "SELECT * FROM students_in_course WHERE user_id=:user_id "
	result = db.session.execute(sql, {"user_id":user_id})
	courses = result.fetchall()
	return courses
