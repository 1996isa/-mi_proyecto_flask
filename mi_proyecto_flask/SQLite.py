from flask_sqlalchemy import SQLAlchemy

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Definir modelo de usuario
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    edad = db.Column(db.Integer)


# Crear la base de datos y las tablas
with app.app_context():
    db.create_all()


# Ruta para agregar usuario
@app.route('/agregar_usuario', methods=['POST'])
def agregar_usuario():
    nombre = request.form['nombre']
    edad = request.form['edad']

    nuevo_usuario = Usuario(nombre=nombre, edad=int(edad))
    db.session.add(nuevo_usuario)
    db.session.commit()

    return "Usuario agregado a la base de datos"


# Ruta para obtener todos los usuarios
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    usuarios = Usuario.query.all()
    lista_usuarios = [{"id": u.id, "nombre": u.nombre, "edad": u.edad} for u in usuarios]
    return jsonify(lista_usuarios)
