import json

# Ruta para guardar datos en JSON
@app.route('/guardar_json', methods=['POST'])
def guardar_json():
    data = request.get_json()
    with open('datos/datos.json', 'w') as file:
        json.dump(data, file)
    return "Datos guardados en JSON"

# Ruta para leer JSON
@app.route('/leer_json', methods=['GET'])
def leer_json():
    with open('datos/datos.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)
