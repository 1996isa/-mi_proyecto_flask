from flask import Flask, request, jsonify
import json
import csv
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de SQLite
db_path = os.path.join(os.path.dirname(__file__), 'database', 'usuarios.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo de base de datos
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    edad = db.Column(db.Integer)

with app.app_context():
    db.create_all()

# Persistencia con TXT
@app.route('/guardar_txt', methods=['POST'])
def guardar_txt():
    data = request.form['contenido']
    with open('datos/datos.txt', 'a') as file:
        file.write(data + '\n')
    return "Datos guardados en TXT"

@app.route('/leer_txt', methods=['GET'])
def leer_txt():
    with open('datos/datos.txt', 'r') as file:
        contenido = file.readlines()
    return jsonify(contenido)

# Persistencia con JSON
@app.route('/guardar_json', methods=['POST'])
def guardar_json():
    data = request.get_json()
    with open('datos/datos.json', 'w') as file:
        json.dump(data, file)
    return "Datos guardados en JSON"

@app.route('/leer_json', methods=['GET'])
def leer_json():
    with open('datos/datos.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)

# Persistencia con CSV
@app.route('/guardar_csv', methods=['POST'])
def guardar_csv():
    nombre = request.form['nombre']
    edad = request.form['edad']
    with open('datos/datos.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nombre, edad])
    return "Datos guardados en CSV"

@app.route('/leer_csv', methods=['GET'])
def leer_csv():
    with open('datos/datos.csv', 'r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return jsonify(data)

# Persistencia con SQLite
@app.route('/agregar_usuario', methods=['POST'])
def agregar_usuario():
    nombre = request.form['nombre']
    edad = request.form['edad']
    nuevo_usuario = Usuario(nombre=nombre, edad=int(edad))
    db.session.add(nuevo_usuario)
    db.session.commit()
    return "Usuario agregado a la base de datos"

@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    usuarios = Usuario.query.all()
    lista_usuarios = [{"id": u.id, "nombre": u.nombre, "edad": u.edad} for u in usuarios]
    return jsonify(lista_usuarios)

if __name__ == '__main__':
    app.run(debug=True)
