from flask import Blueprint, flash, render_template, request
import pymongo

client = pymongo.MongoClient("mongodb+srv://oemerfurkan:123321@cluster0.ocu6zjv.mongodb.net/?retryWrites=true&w=majority")
db = client.users
collection = db.username_password

views = Blueprint('views', __name__)

@views.route("/")
def home():
    return render_template("base.html")

@views.route('/register',methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(username) < 5:
            return render_template("register_error.html")
        elif password1 != password2:
            return render_template("register_error.html")
        elif len(password1) < 7:
            return render_template("register_error.html")
        else:
            user = {"username" : f"{username}", "password" : f"{password1}"}
            collection.insert_one(user)
            return render_template("success_register.html")

    return render_template('register.html')

@views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user_control = collection.find_one({"username" : f"{username}", "password" : f"{password}"})
        if user_control == None:
            flash("Hatalı kullanıcı adı veya şifre")
            return render_template("register.html")
        else:
            return render_template("success_login.html")
    return render_template("login.html")