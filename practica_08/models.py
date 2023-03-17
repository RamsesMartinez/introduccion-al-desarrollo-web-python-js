from flask_login import UserMixin

# Implementación personalizada de UserMixin
class User(UserMixin):
    def __init__(self, username, password):
        self.id = username
        self.password = password

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

users = {
    'john': User('john', 'password'),
    'susan': User('susan', 'password')
    }

