from app import app
from flask import redirect, render_template, request, session
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash
import users

app.secret_key = getenv("SECRET_KEY")


@app.route("/")
def index():
	return render_template("index.html")


#kirjaudutaan sisään
@app.route("/login",methods=["GET", "POST"])
def login():
	if request.method == "GET":
		return render_template("index.html")
	if request.method == "POST":
		username = request.form["username"]
		password = request.form["password"]   
		if users.get_user(username, password):
			return render_template("/profile.html")
			#oikeasti"/profiles/<int:id>"
		else:
			return render_template("error.html", error="Väärä tunnus tai salasana")
 
	
#tähän luo käyttäjä sivusto
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
			
	#admin?
	
#tarkastetaan saako käyttäjä nähdä profiilin
@app.route("/profile/<int:id>")
def profile(id):
	allow = False
	if users.is_admin():
		allow = True
	elif users.is_admin == False and user_id() == id:
		allow = True
	if not allow:
		return render_template("error.html", error="Ei oikeutta nähdä sivua")
	if allow:
		return redirect("/profile/"+ str(id))

