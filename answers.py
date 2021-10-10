from db import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask import session
import routes


def add_answer(task_id, task_topic, student_id, content, course_id):
	sql = "INSERT INTO answers (task_id, task_topic, student_id, content, course_id, sent_at) VALUES (:task_id, :task_topic, :student_id, :content, :course_id, NOW())"
	db.session.execute(sql, {"task_id":task_id, "task_topic":task_topic, "student_id":student_id, "content":content, "course_id":course_id})
	db.session.commit()

def find_answer(task_id, student_id, course_id):
	sql = "SELECT * FROM answers WHERE task_id=:task_id and student_id=:student_id and course_id=:course_id"
	result = db.session.execute(sql, {"task_id":task_id, "student_id":student_id, "course_id":course_id})
	found = result.fetchone()
	if found:
		return found
	else:
		return False
def get_all(student_id):
	sql = "SELECT * FROM answers WHERE student_id=:student_id"
	result = db.session.execute(sql, {"student_id":student_id})
	all = result.fetchall()
	return all


