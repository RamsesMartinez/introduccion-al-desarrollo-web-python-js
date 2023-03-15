from flask import Flask, render_template, request, redirect

app = Flask(__name__)

libros = []

@app.route('/')
def index():
    return render_template('formulario.html')

@app.route('/', methods=['POST'])
def agregar_libro():
    titulo = request.form['titulo']
    autor = request.form['autor']
    genero = request.form['genero']

    libro = {'titulo': titulo, 'autor': autor, 'genero': genero}
    libros.append(libro)

    return redirect('/lista_libros')

@app.route('/lista_libros')
def lista_libros():
    return render_template('lista_libros.html', libros=libros)

if __name__ == '__main__':
    app.run(debug=True)
