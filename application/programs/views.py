from application import app, db
from flask import render_template, request, url_for, redirect
from flask_login import login_required, current_user

from application.programs.models import Programs
from application.programs.forms import ProgramForm, ProgramFilterForm


@app.route("/programs/", methods=["GET"])
@login_required
def programs_index():
    created_by = request.args.get('createdBy')

    if (created_by == None):
        p = Programs.find_programs_by_creators_name("")
    else:
        p = Programs.find_programs_by_creators_name(created_by)

    return render_template("programs/list.html", programs = p, form = ProgramFilterForm())

@app.route("/programs/new/")
@login_required
def programs_form():
    return render_template("programs/new.html", form = ProgramForm())

@app.route("/programs/", methods=["POST"])
@login_required
def programs_create():
    form = ProgramForm(request.form)

    if not form.validate():
        return render_template("programs/new.html", form = form)

    p = Programs(current_user.id, form.name.data, form.description.data)

    db.session().add(p)
    db.session().commit()

    return redirect(url_for("programs_index"))


#delete this
@app.route("/programs/asd", methods=["GET"])
@login_required
def programs_create2():
    program = Programs(current_user.id, "nimi", "kuvaus")
    db.session().add(program)
    db.session().commit()

    return redirect(url_for("events_list"))

