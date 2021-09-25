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
		if (user_id):
			session["username"] = username
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
		hash_value = generate_password_hash(password)
		if users.create_user(username, hash_value):
			return redirect("/signup")
		else:
			return render_template("error.html", error="Creating account was unsuccessfull")
			

	
@app.route("/profile/<int:id>")
def profile(id):
	allow = False
	if users.is_admin(id):
		allow = True
	elif users.is_user and users.user_id() == id:
		allow = True
	if not allow:
		return render_template("error.html", error="Ei oikeutta nähdä sivua")
	if allow:
		return render_template("profile.html")


@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")


@app.route("/courses")
def courses():
	all = modify_courses.all_courses()
	admin = users.is_admin(session["user_id"])
	return render_template("courses.html", courses = all, admin = admin)

@app.route("/add_course", methods=["GET", "POST"])
def add_course():
	if request.method == "GET":
		allow = False
		if users.is_admin(session["user_id"]):
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
	if request.method == "GET":
		attending = modify_courses.attending(id, session["user_id"])
		return render_template("course.html", attending = attending)
	if request.method == "POST":
		modify_courses.attend_course(id, session["user_id"])
		return redirect("/courses/" + str(id))
