from db import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask import session
import routes

def add_text(course_id, topic, content):
	sql = "INSERT INTO course_text (course_id, topic, content) VALUES (:course_id, :topic, :content)"
	db.session.execute(sql, {"course_id":course_id, "topic":topic, "content":content})
	db.session.commit()

def get_all(course_id):
	sql = "SELECT * FROM course_text WHERE course_id=:course_id"
	result = db.session.execute(sql, {"course_id":course_id})
	course_text = result.fetchall()
	return course_text
