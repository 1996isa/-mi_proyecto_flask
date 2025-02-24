<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{% block title %} {% endblock %} - Mi Proyecto Flask</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <nav>
        <a href="{{ url_for('index') }}">Inicio</a>
        <a href="{{ url_for('about') }}">Acerca de</a>
    </nav>
    <div class="content">
        {% block content %} {% endblock %}
    </div>
</body>
</html>