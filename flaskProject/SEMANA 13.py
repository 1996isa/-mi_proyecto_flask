from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return '¡Hola, Mundo!'

    if __name__ == '__main__':
        app.run(debug=True)

import mysql.connector

    def obtener_conexion():
        try:
            conexion = mysql.connector.connect(
                host='localhost',
                user='root',
                password='tu_contraseña',
                database='desarrollo_web'
            )
            return conexion
        except mysql.connector.Error as error:
            print("Error al conectar a MySQL:", error)
            return None
from flask import Flask
    from Conexion import conexion

    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return '¡Hola, Mundo!'

    @app.route('/test_db')
    def test_db():
        db = conexion.obtener_conexion()
        if db:
            db.close()
            return 'Conexión a MySQL exitosa'
        else:
            return 'Error al conectar a MySQL'

    if __name__ == '__main__':
        app.run(debug=True)

USE desarrollo_web;

    CREATE TABLE usuarios (
        id_usuario INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(255),
        mail VARCHAR(255)