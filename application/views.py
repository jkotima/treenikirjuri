from flask import render_template
from application import app
from application.sets.models import Sets
from flask_login import current_user


@app.route("/")
def index():
    if current_user.is_authenticated:
        return render_template("index.html",
                               amountlifted=Sets.find_total_lifted(
                                   current_user.id))
    else:
        return render_template("index.html", amountlifted=0)
