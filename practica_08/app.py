from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import users
from forms import BookForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'LLAVE_SUPER_SECRETA'

# Crea una instancia de LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'index'

books = []

# Función para cargar el usuario por ID
@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)


# Ruta de inicio de sesión
@app.route('/', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('list_books'))
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = users.get(username)
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('list_books'))
    return render_template('login.html', form=form)


# Ruta de cierre de sesión
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/create_book', methods=['GET', 'POST'])
@login_required
def create_book():
    form = BookForm()
    if form.validate_on_submit():
        title = form.title.data
        author = form.author.data
        books.append({'title': title, 'author': author})
        return redirect(url_for('list_books'))
    return render_template('create_book.html', form=form)


@app.route('/books')
@login_required
def list_books():
    return render_template('list_books.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
