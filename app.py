from flask import Flask, render_template, redirect, url_for, request
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os
from modules.usuario import Usuario
load_dotenv()

app = Flask(__name__)
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/registrar-usuario', methods=['POST'])
def FormRegistro():
    usuario = Usuario(mysql)
    
    if request.method == 'POST':
        nombre     = request.form['nombre']
        email      = request.form['email']
        contrasena = request.form['password']

        print(nombre, email, contrasena)
        
        if usuario.RegistrarUsuario(nombre, email, contrasena):
            return "Usuario registrado"
        else:
            return "Error al registrar el usuario"

    return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.run(port=5000, debug=True)
