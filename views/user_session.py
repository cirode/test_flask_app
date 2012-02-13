from flaskext.login import login_user, logout_user, login_required
from flask import render_template, current_app, redirect, request, url_for
from forms import LoginForm

def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_user(form.user())
        return redirect(request.args.get("next") or url_for("home"))
    return render_template('login.html', form=form)

@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))