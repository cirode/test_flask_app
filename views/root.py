from flask import current_app,render_template
from flaskext import login

@login.login_required
def home_page():
    return render_template('show_config.html', config=current_app.config)

    