from db import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask import session
import routes


def add_answer(task_id, task_topic, student_id, content):
	sql = "INSERT INTO answers (task_id, task_topic, student_id, content, sent_at) VALUES (:task_id, :task_topic, :student_id, :content, NOW())"
	db.session.execute(sql, {"task_id":task_id, "task_topic":task_topic, "student_id":student_id, "content":content})
	db.session.commit()

def find_answer(task_id, student_id):
	sql = "SELECT * FROM answers WHERE task_id=:task_id and student_id=:student_id"
	result = db.session.execute(sql, {"task_id":task_id, "student_id":student_id})
	found = result.fetchone()
	if found:
		return True
	else:
		return False
def get_all(student_id):
	sql = "SELECT * FROM answers WHERE student_id=:student_id"
	result = db.session.execute(sql, {"student_id":student_id})
	all = result.fetchall()
	return all
