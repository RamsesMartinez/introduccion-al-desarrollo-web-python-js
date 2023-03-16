from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

csrf = CSRFProtect(app)


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=30)])
    submit = SubmitField('Login')


@app.route('/welcome')
def index():
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if username != 'username' or password != 'password':
            flash('Credenciales inválidas', 'error')
            return render_template('login.html', form=form)
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
