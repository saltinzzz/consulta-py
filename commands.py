from flask import Flask
from extensions import db
from models import Usuario
from werkzeug.security import generate_password_hash

def init_app(app: Flask):

    @app.cli.command("create-db")
    def create_db():
        """Crea la base de datos"""
        with app.app_context():
            db.drop_all()
            db.create_all()
            print("✔ Base de datos creada correctamente.")

    @app.cli.command("crear-usuario")
    def crear_usuario():
        """Crear un usuario administrador por consola."""
        with app.app_context():
            usuario = input("Nombre de usuario: ")
            password = input("Contraseña: ")
            sucursal = input("Sucursal: ")

        # Validar duplicado
        existe = Usuario.query.filter_by(usuario=usuario).first()
        if existe:
            print("❌ Ese usuario ya existe")
            return

        nuevo = Usuario(
            usuario=usuario,
            sucursal=sucursal
        )
        nuevo.set_password(password)  # <<< ESTA ES LA MANERA CORRECTA

        db.session.add(nuevo)
        db.session.commit()

        print("✔ Usuario creado exitosamente")

