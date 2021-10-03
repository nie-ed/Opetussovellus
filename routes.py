from app import app
from flask import redirect, render_template, request, session
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash
import users
from flask import Flask
import modify_courses


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
			return redirect("/profile/" + str(user_id))
		else:
			return render_template("error.html", error="Väärä tunnus tai salasana")
 
	
@app.route("/signup", methods=["GET", "POST"])
def create_account():
	if request.method == "GET":
		return render_template("signup.html")
	if request.method == "POST":
		username = request.form["username"]
		password = request.form["password"]
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
		if users.is_admin(user_id):
			allow = True
		if users.is_user(user_id) and user_id == id:
			allow = True
		if not allow:
			return render_template("error.html", error="Ei oikeutta nähdä sivua")
		if allow:
			return render_template("profile.html")
		
		
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
		name = request.form["name"]
		modify_courses.add_course(name)
		return redirect ("/courses")
		
		
@app.route("/courses/<int:id>", methods=["GET", "POST"])
def course_site(id):
	user_id = session["user_id"]
	admin = users.is_admin(user_id)
	if request.method == "GET":
		attending = modify_courses.attending(id, user_id)
		if attending or admin:
			return render_template("course.html", admin=admin)
		else:
			course = modify_courses.get_course(id)
			return render_template("attend_course.html", course = course)
	if request.method == "POST":
		modify_courses.attend_course(id, user_id)
		attending = modify_courses.attending(id, user_id)
		if attending:
			return render_template("course.html", admin=admin)
		else:
			return render_template("error.html", error="Kurssille ilmottautuminen ei onnistunut")


@app.route("/modify_course")
def modify_course():
	return render_template("modify_course.html")
