from flaskext.wtf import Form, TextField, PasswordField, validators, ValidationError
from models import user_model

class LoginForm(Form):
    def _check_user(form, field):
        user = form.user()
        if not user:
            raise ValidationError('The Username / Password combination you have entered do not match')
    
    def user(self):
        return user_model.User.get_authenticated_user(self.username.data, self.password.data)
            
    username = TextField('Username', [validators.Length(min=0, max=25), _check_user])
    password = PasswordField('New Password', [
        validators.Required()
    ])
    