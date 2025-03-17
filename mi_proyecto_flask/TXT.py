from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Ruta para escribir en un archivo TXT
@app.route('/guardar_txt', methods=['POST'])
def guardar_txt():
    data = request.form['contenido']
    with open('datos/datos.txt', 'a') as file:
        file.write(data + '\n')
    return "Datos guardados en TXT"

# Ruta para leer el archivo TXT
@app.route('/leer_txt', methods=['GET'])
def leer_txt():
    with open('datos/datos.txt', 'r') as file:
        contenido = file.readlines()
    return jsonify(contenido)

if __name__ == '__main__':
    app.run(debug=True)
