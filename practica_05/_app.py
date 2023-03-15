from flask import Flask, request 

app = Flask(__name__)

@app.route('/formulario', methods=['POST']) 
def procesar_formulario(): 
    nombre = request.form['nombre'] 
    email = request.form['email'] 
    # Lógica para procesar el formulario aquí 
    
    return f'Tu nombre es {nombre} y tu email es {email}' 

if __name__ == '__main__': 
    app.run()
