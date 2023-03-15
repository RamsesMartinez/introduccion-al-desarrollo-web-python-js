from flask import Flask, request, render_template


app = Flask(__name__)

@app.route("/hello/<string:nombre>", methods=["GET"])
def hello_world(nombre):
    return f"Hello, {nombre}, from GET function!"


@app.route("/hello/<string:nombre>", methods=["POST"])
def hello_world_post(nombre):
    return f"Hello, {nombre}, from POST function!"


@app.route("/formulario", methods=["POST"])
def procesar_formulario():
    # lÓGICA DEL FORMULARIO
    nombre = request.form["nombre"]
    email = request.form["email"]
    return f"Hola {nombre}! tu correo es {email}"


@app.route("/saludar/<string:nombre>", methods=["GET"])
def saludar(nombre):
    return render_template("saludo.html", nombree=nombre)
    # return f"<h1>Hola {nombre}</h1>"



if __name__ == '__main__':
    app.run(debug=True)
