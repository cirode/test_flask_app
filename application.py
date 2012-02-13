from flask import Flask, current_app
import os
from views import root, user_session #add an auto-loader here, all modules need to be loaded
from models import user_model
from lib import utils
from flaskext import login

app = Flask(__name__,static_url_path='')
app.config['ENVIRONMENT'] = os.environ.get('FLASK_ENVIRONMENT') or 'development'
app.config.from_object('config.default') 
app.config.from_object('config.{environment}'.format(environment=app.config["ENVIRONMENT"]))#Load the environment specific config

login_manager = login.LoginManager()
login_manager.setup_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def user_loader(user_id):
    return user_model.User(username=user_id) if user_id else None

@app.before_request
def before_request():
    #get db connection
    pass

@app.teardown_request
def teardown_request(exception):
    #release connection
    pass

@app.context_processor
def override_url_for():
    return dict(url_for=utils.dated_url_for)

app.add_url_rule('/', 'home', view_func=root.home_page)
app.add_url_rule('/login', 'login', view_func=user_session.login,  methods=["GET", "POST"])
app.add_url_rule('/logout', 'logout', view_func=user_session.logout,  methods=["GET", "DELETE"])

    
if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], host=app.config['HOST'], port=app.config['PORT'])