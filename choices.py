from db import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask import session


def add_choice(task_id, choice_text):
	sql = "INSERT INTO choices (task_id, choice_text) VALUES (:task_id, :choice_text)"
	db.session.execute(sql, {"task_id":task_id, "choice_text":choice_text})
	db.session.commit()

def get_all_course_question_id(course_id):
	sql = "SELECT id FROM tasks WHERE course_id= course_id"
	result = db.session.execute(sql, {"course_id":course_id})
	all_question_id = result.fetchall()
	return all_question_id

def get_all_choices(task_id):
	sql = "SELECT id, choice_text FROM choices WHERE task_id=:task_id"
	result = db.session.execute(sql, {"task_id":task_id})
	choices = result.fetchall()
	return choices

def get_choice(id):
	sql = "SELECT choice_text FROM choices WHERE id=:id"
	result = db.session.execute(sql, {"id":id})
	choice = result.fetchone()[0]
	if choice:
		return choice
	else:
		return False
