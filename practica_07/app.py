from flask import Flask, render_template, redirect, url_for

from forms import BookForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'LLAVE_SUPER_SECRETA'

books = []

@app.route('/')
def index():
    return redirect(url_for("list_books"))

@app.route('/create_book', methods=['GET', 'POST'])
def create_book():
    form = BookForm()
    if form.validate_on_submit():
        title = form.title.data
        author = form.author.data
        books.append({'title': title, 'author': author})
        return redirect(url_for('list_books'))
    return render_template('create_book.html', form=form)

@app.route('/books')
def list_books():
    return render_template('list_books.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
