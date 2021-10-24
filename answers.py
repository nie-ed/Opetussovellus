from db import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask import session
import routes


def add_answer(task_id, student_id, content, course_id):
	sql = "INSERT INTO answers (task_id, student_id, content, course_id, sent_at) VALUES (:task_id, :student_id, :content, :course_id, NOW())"
	db.session.execute(sql, {"task_id":task_id,"student_id":student_id, "content":content, "course_id":course_id})
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


def get_all_task_answers(task_id):
	sql = "SELECT t.text_question, a.content, u.username" \
	" FROM tasks t, answers a, users u " \
	"WHERE a.task_id=:task_id and a.student_id=u.id and t.id=:task_id"
	result = db.session.execute(sql,{"task_id":task_id})
	all = result.fetchall()
	return all


def get_all_choice_answers(task_id):
	sql = "SELECT c.choice_text, u.username FROM choices c, " \
	"choice_student_answers s, users u WHERE c.id=s.choice_id and " \
	"s.task_id=:task_id and s.student_id=u.id"
	result = db.session.execute(sql, {"task_id":task_id})
	all = result.fetchall()
	return all

def add_choice_student_answer(task_id, choice_id, student_id):
	sql = "INSERT INTO choice_student_answers (task_id, choice_id, student_id) VALUES (:task_id, :choice_id, :student_id)"
	db.session.execute(sql, {"task_id":task_id, "choice_id":choice_id, "student_id":student_id})
	db.session.commit()

def find_choice_answer(task_id, student_id):
	sql = "SELECT choice_id FROM choice_student_answers WHERE task_id=:task_id and student_id=:student_id"
	result = db.session.execute(sql, {"task_id":task_id, "student_id":student_id})
	choice_id = result.fetchone()
	if choice_id:
		return choice_id
	else:
		return False

def find_student_answer(student_id):
	sql = "SELECT users.username, answers.content FROM users, answers WHERE users.id = student_id AND answers.student_id = users.id"
	result = db.session.execute(sql, {"student_id":student_id})
	answer = result.fetchall()
	return answer

def count_student_answered(task_id, student_id):
	sql = "SELECT COUNT(*) FROM answers WHERE task_id=:task_id AND student_id=:student_id"
	result = db.session.execute(sql, {"task_id":task_id, "student_id":student_id})
	amount = result.fetchone()[0]
	return amount

def count_student_choice_answered(task_id, student_id):
	sql = "SELECT COUNT(*) FROM choice_student_answers WHERE task_id=:task_id AND student_id=:student_id"
	result = db.session.execute(sql, {"task_id":task_id, "student_id":student_id})
	amount = result.fetchone()[0]
	return amount


def choice_correct_answer(task_id, choice_id):
	sql = "INSERT INTO choice_correct_answers (choice_id, task_id) VALUES (:choice_id, :task_id)"
	db.session.execute(sql, {"choice_id":choice_id, "task_id":task_id})
	db.session.commit()

def find_choice_correct_answer(task_id):
	sql = "SELECT c.choice_text, c.id FROM choices c, choice_correct_answers a WHERE c.id=a.choice_id and a.task_id=:task_id"
	result = db.session.execute(sql, {"task_id":task_id})
	correct = result.fetchone()
	return correct
