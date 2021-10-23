from db import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask import session
import routes


def add_task(text_question, course_id, multiple_choice):
	sql = "INSERT INTO tasks (text_question, course_id, multiple_choice) VALUES (:text_question, :course_id, :multiple_choice) RETURNING id"	
	result = db.session.execute(sql, {"text_question":text_question, "course_id":course_id, "multiple_choice":multiple_choice})
	task_id = result.fetchone()[0]
	db.session.commit()
	return task_id

def get_task(id):
	sql = "SELECT * FROM tasks WHERE id=:id"
	result = db.session.execute(sql, {"id":id})
	task = result.fetchone()
	return task


def get_all(course_id):
	sql = "SELECT * FROM tasks WHERE course_id=:course_id"
	result = db.session.execute(sql, {"course_id":course_id})
	tasks = result.fetchall()
	return tasks


def get_course_id(id):
	sql = "SELECT course_id FROM tasks WHERE id=:id"
	result = db.session.execute(sql, {"id":id})
	course_id = result.fetchone()
	return course_id
