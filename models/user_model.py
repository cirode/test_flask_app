from flaskext.login import UserMixin

class User(UserMixin):
    def __init__(self,username=None):
        self.username = username
        self.id = username
    
    @staticmethod
    def get_authenticated_user(username, password):
        return User(username=username)
        