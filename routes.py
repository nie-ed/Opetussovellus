from app import app
from flask import redirect, render_template, request, session
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash
import users
from flask import Flask
import modify_courses
import modify_tasks
import answers
import modify_text
import secrets
import choices

app.secret_key = getenv("SECRET_KEY")


@app.route("/")
def index():
	return render_template("index.html")


@app.route("/login",methods=["GET", "POST"])
def login():
	if request.method == "GET":
		return render_template("index.html")
	if request.method == "POST":
		username = request.form["username"]
		password = request.form["password"]   
		user_id = users.get_user(username, password)
		if user_id:
			session["username"] = username
			session["user_id"] = user_id
			session["csrf_token"] = secrets.token_hex(16)
			return redirect("/main_page")
		else:
			return render_template("error.html", error="Väärä tunnus tai salasana")
 
@app.route("/main_page")
def main_page():
	return render_template("main_page.html")

@app.route("/signup", methods=["GET", "POST"])
def create_account():
	if request.method == "GET":
		return render_template("signup.html")
	if request.method == "POST":
		username = request.form["username"]
		password = request.form["password"]
		password2 = request.form["password2"]
		if not password == password2:
			return render_template("error.html", error="Typed in two different passwords")
		if len(username) > 30 or len(username) < 1:
			return render_template("error.html", error="Nimi on liian pitkä tai lyhyt")
		if len(password) > 50 or len(password) < 4:
			return render_template("error.html", error="Salasana on liian pitkä tai lyhyt")
		else:
			hash_value = generate_password_hash(password)
			if users.create_user(username, hash_value):
				return redirect("/")
			else:
				return render_template("error.html", error="Creating account was unsuccessfull")
			
@app.route("/profile")
def profile_route():
	return redirect("profile/" + str(session["user_id"]))

	
@app.route("/profile/<int:id>")
def profile(id):
	if request.method == "GET":
		user_id = session["user_id"]
		allow = False
		admin = users.is_admin(user_id)
		if users.is_admin(user_id):
			allow = True
		if users.is_user(user_id) and user_id == id:
			allow = True
		if not allow:
			return render_template("error.html", error="Ei oikeutta nähdä sivua")
		if allow:
			students_courses = []
			courses_attending = modify_courses.user_attends(session["user_id"])
			courses_created = modify_courses.get_courses_user_created(session["user_id"])
			for course in courses_attending:
				students_courses.append(modify_courses.get_course(course.course_id))
			return render_template("profile.html", students_courses=students_courses, admin =admin, courses_created = courses_created)
		
		
@app.route("/logout")
def logout():
	del session["username"]
	del session["user_id"]
	return redirect("/")

@app.route("/courses")
def courses():
	all = modify_courses.all_courses()
	admin = users.is_admin(session["user_id"])
	return render_template("courses.html", courses = all, admin = admin)

@app.route("/add_course", methods=["GET", "POST"])
def add_course():
	if request.method == "GET":
		user_id = session["user_id"]
		allow = False
		if users.is_admin(user_id):
			allow = True
		if not allow:
			return render_template("error.html", error="Ei oikeutta nähdä sivua")
		if allow:
			return render_template("add_course.html")
	if request.method == "POST":
		if session["csrf_token"] != request.form["csrf_token"]:
			abort(403)

		else:
			name = request.form["name"]
			if len(name) > 100 or len(name) < 2:
				return render_template("error.html", error="Nimi on liian pitkä tai lyhyt")
			modify_courses.add_course(name, session["user_id"])
			return redirect ("/courses")
		
		
@app.route("/courses/<int:id>", methods=["GET", "POST"])
def course_site(id):
	user_id = session["user_id"]
	admin = users.is_admin(user_id)
	course = modify_courses.get_course(id)
	tasks=modify_tasks.get_all(id)
	content = modify_text.get_all(id)
	tasks=modify_tasks.get_all(id)
	amount_tasks = len(tasks)
	amount_answered = 0
	for task in tasks:
		amount_answered = amount_answered + answers.count_student_answered(task.id, user_id)

	if request.method == "GET":
		attending = modify_courses.attending(id, user_id)
		if attending or admin:
			return render_template("course.html", content = content, admin=admin, id = id, course = course, student_id = user_id, amount_answered = amount_answered, amount_tasks=amount_tasks, tasks = tasks)
		else:
			course = modify_courses.get_course(id)
			return render_template("attend_course.html", course = course)
	if request.method == "POST":
		if session["csrf_token"] != request.form["csrf_token"]:
			abort(403)

		else:
			modify_courses.attend_course(id, user_id)
			attending = modify_courses.attending(id, user_id)
			if attending:
				return render_template("course.html", content = content, admin=admin, id = id, course = course, student_id = user_id, amount_answered = amount_answered, amount_tasks=amount_tasks, tasks = tasks)
			else:
				return render_template("error.html", error="Kurssille ilmottautuminen ei onnistunut")

@app.route("/question/<int:id>", methods=["GET", "POST"])
def question_site(id):
	if request.method == "GET":
		return render.template("question.html")
	
	if request.method == "POST":
		if session["csrf_token"] != request.form["csrf_token"]:
			abort(403)
		else:
			user_id = session["user_id"]
			course_id = request.form["course_id"]
			course = modify_courses.get_course(course_id)
			task=modify_tasks.get_task(id)
			choice_id = answers.find_choice_answer(id, user_id)
			choice_answer = False
			is_correct = "incorrectly"
			correct_answer=False
			if choice_id:
				choice_answer = choices.get_choice(choice_id.choice_id)
				if (choice_answer):
					correct_answer = answers.find_choice_correct_answer(id)
					if (correct_answer.id == choice_id.choice_id):
						is_correct = "correctly"
			all_choices = choices.get_all_choices(id)
			answer = answers.find_answer(id, user_id, course_id)
			return render_template("question.html", task = task, all_choices=all_choices, answer = answer, course = course, choice_answer=choice_answer, correct_answer = correct_answer, is_correct = is_correct)


@app.route("/students_attending_course", methods=["POST"])
def students_attending_course():
	if session["csrf_token"] != request.form["csrf_token"]:
		abort(403)

	else:
		course_id = request.form["course_id"]
#		student_id = request.form["student_id"]
		attending = modify_courses.all_students_in_course(course_id)
		return render_template("students_attending_course.html", attending = attending)

@app.route("/modify_course", methods=["POST"])
def modify_course():
	if session["csrf_token"] != request.form["csrf_token"]:
		abort(403)

	else:
		id = request.form["id"]
		return render_template("modify_course.html", id = id)


@app.route("/create_new_question", methods=["POST"])
def create_new_question():
	if session["csrf_token"] != request.form["csrf_token"]:
		abort(403)

	else:
		if request.method == "POST":
			course_id = request.form["course_id"]
			text_question = request.form["text_question"]
			if len(text_question) > 100  or len(text_question) <2:
				return render_template("error.html", error="Question is too short or long")
			multiple_choice = False
			modify_tasks.add_task(text_question, course_id, multiple_choice)
			return redirect("/courses/" + str(course_id))


@app.route("/create_new_content", methods=["POST"])
def create_new_content():
	if request.method == "POST":
	
		if session["csrf_token"] != request.form["csrf_token"]:
			abort(403)

		else:
			course_id = request.form["course_id"]
			topic = request.form["topic"]
			if len(topic) > 100  or len(topic) <2:
				return render_template("error.html", error="Topic is too short or long")
			content = request.form["content"]
			if len(content) > 2000  or len(content) <10:
				return render_template("error.html", error="Text content is too short or long")
			modify_text.add_text(course_id, topic, content)
			return redirect("/courses/" + str(course_id))

@app.route("/create_new_multiple_choice_question", methods=["POST"])
def create_new_multiple_choice_question():
		if session["csrf_token"] != request.form["csrf_token"]:
			abort(403)

		else:
			task_topic = request.form["text_question"]
			if len(task_topic) > 100  or len(task_topic) <2:
                        	return render_template("error.html", error="Question is too short or long")
			course_id = request.form["course_id"]
			multiple_choice = True
			task_id = modify_tasks.add_task(task_topic, course_id, multiple_choice)
			task_choices =  request.form.getlist("choice")
			for choice in task_choices:
				if choice != "":
					choices.add_choice(task_id, choice, task_topic)
			return redirect("/correct_answer/" + str(task_id))

@app.route("/correct_answer/<int:id>", methods = ["GET", "POST"])
def correct_answer(id):
	task_id = id
	course_id = modify_tasks.get_course_id(id)
	if request.method == "GET":
		task_choices = choices.get_all_choices(task_id)
		return render_template("correct_answer.html", task_id = task_id, task_choices = task_choices)
	if request.method == "POST":
		if session["csrf_token"] != request.form["csrf_token"]:
			abort(403)

		else:
			student_id = session["user_id"]
			if "answer" in request.form:
				choice_id = request.form["answer"]
				answers.choice_correct_answer(task_id, choice_id)
			return redirect("/courses/" +str(course_id.course_id))

@app.route("/add_choice_answer", methods=["POST"])
def add_choice_answer():
	if session["csrf_token"] != request.form["csrf_token"]:
		abort(403)
	
	else:
		task_id = request.form["task_id"]
		student_id = session["user_id"]
		if "answer" in request.form:
			choice_id = request.form["answer"]
			answers.add_choice_student_answer(task_id, choice_id, student_id)
		return redirect("/courses")

@app.route("/add_answer", methods=["POST"])
def add_answer():
	if request.method == "POST":
		if session["csrf_token"] != request.form["csrf_token"]:
			abort(403)
		else:
			task_id = request.form["task_id"]
			student_id = session["user_id"]
			content = request.form["content"]
			if len(content) > 300  or len(content) <5:
				return render_template("error.html", error="Answer is too long or short. Answer should be between 5-300 characters")
			task_topic = request.form["topic"]
			course_id = request.form["course_id"]
			answers.add_answer(task_id, task_topic, student_id, content=content, course_id=course_id)
			return redirect("/courses")
 
@app.route("/student_answers", methods = ["POST"])
def student_answers():
	if session["csrf_token"] != request.form["csrf_token"]:
		abort(403)

	else:
		task_id = request.form["task_id"]
		course_id = request.form["course_id"]
		course = modify_courses.get_course(course_id)
		all_answers = answers.get_all_task_answers(task_id)
		return render_template("student_answers.html", all_answers = all_answers, course=course)
	#puuttuu vielä monivalinta

@app.route("/delete_course/<int:id>")
def delete_course_id(id):
	course = modify_courses.get_course(id)
	return render_template("delete_course.html", course = course)
	
@app.route("/delete_course", methods = ["POST"])
def delete_course():
	if session["csrf_token"] != request.form["csrf_token"]:
		abort(403)

	else:
		course_id = request.form["course_id"]
		modify_courses.delete_course(course_id)
		return redirect("/courses")
