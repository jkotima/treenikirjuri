from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import Users
from application.auth.forms import LoginForm, RegisterForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = Users.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/register", methods = ["GET", "POST"])
def auth_register():    
    if request.method == "GET":
        return render_template("auth/registerform.html", form = RegisterForm())
    
    form = RegisterForm(request.form)
    
    # validointi
    usr = Users.query.filter_by(username=form.username.data, password=form.password.data).first()
    if usr:
        return render_template("auth/registerform.html", form = form, error = "Account already exists")  


    u = Users(form.name.data, form.username.data, form.password.data)
    
    db.session().add(u)
    db.session().commit()

    return redirect(url_for("index"))  


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))