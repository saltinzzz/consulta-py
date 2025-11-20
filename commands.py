from extensions import db
from app import app
import click

@app.cli.command("create-db")
def create_db():
    with app.app_context():
        db.create_all()
        click.echo("Base de datos creada correctamente")
