from flask_login import UserMixin

# Implementación personalizada de UserMixin
class User(UserMixin):
    def __init__(self, username, nombre, password):
        self.id = username
        self.nombre = nombre
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
    'john': User('john', "Jhon", 'password'),
    'susan': User('susan', "Susan", 'password'),
    'ramses': User('ramses', "Ramses Martinez", 'password'),
    }

