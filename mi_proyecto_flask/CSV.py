import csv


# Ruta para guardar datos en CSV
@app.route('/guardar_csv', methods=['POST'])
def guardar_csv():
    nombre = request.form['nombre']
    edad = request.form['edad']

    with open('datos/datos.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nombre, edad])

    return "Datos guardados en CSV"


# Ruta para leer CSV
@app.route('/leer_csv', methods=['GET'])
def leer_csv():
    with open('datos/datos.csv', 'r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]

    return jsonify(data)
