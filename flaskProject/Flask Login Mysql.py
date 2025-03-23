from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'clave_secreta'

# Configuración de MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''  # Cambia esto por tu contraseña de MySQL
app.config['MYSQL_DB'] = 'desarrollo_web'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

# Configuración de Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


# Modelo de usuario
class Usuario(UserMixin):
    def __init__(self, id, nombre, email, password):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.password = password


@login_manager.user_loader
def load_user(user_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuarios WHERE id_usuario = %s", (user_id,))
    user = cur.fetchone()
    cur.close()
    if user:
        return Usuario(user['id_usuario'], user['nombre'], user['email'], user['password'])
    return None


# Ruta de inicio
@app.route('/')
def index():
    return "Bienvenido al sistema de autenticación con Flask"


# Ruta de registro
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO usuarios (nombre, email, password) VALUES (%s, %s, %s)", (nombre, email, password))
        mysql.connection.commit()
        cur.close()

        flash('Registro exitoso. Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('login'))
    return render_template('registro.html')


# Ruta de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
        user = cur.fetchone()
        cur.close()

        if user and check_password_hash(user['password'], password):
            usuario = Usuario(user['id_usuario'], user['nombre'], user['email'], user['password'])
            login_user(usuario)
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Credenciales incorrectas', 'danger')
    return render_template('login.html')


# Ruta protegida
@app.route('/dashboard')
@login_required
def dashboard():
    return f"Hola, {current_user.nombre}. Bienvenido a tu panel."


# Ruta de cierre de sesión
@app.route('/logout')
def logout():
    logout_user()
    flash('Has cerrado sesión', 'success')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
