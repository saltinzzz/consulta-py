from flask import Flask, render_template, redirect, url_for, flash
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'clave-demo')

pacientes = [
    {"id": 1, "nombre": "Pedro Gomez", "dni": "12345678", "telefono": "987654321","direccion": "Av. Perukistan","fecha_nacimiento": "2000-10-31"},
    {"id": 2, "nombre": "Adriana Tenorio", "dni": "87654321", "telefono": "912345678","direccion": "Calle Besique 444","fecha_nacimiento": "1980-06-31"},
]

consultas = [
    {"id": 1, "paciente": "Pedro Gomez", "motivo": "Dolor de cabeza", "fecha": "2025-10-01","descripcion": "El paciente presenta dolor de cabeza persistente desde hace 3 días. Se recomienda descanso y análisis clínico básico."},
    {"id": 2, "paciente": "Adriana Tenorio", "motivo": "Chequeo general", "fecha": "2025-10-31","descripcion": "Chequeo general anual. No presenta síntomas significativos, se realizaron exámenes de control preventivo."},
]

@app.route('/')
def index():
    return redirect(url_for('listar_pacientes'))

@app.route('/pacientes')
def listar_pacientes():
    return render_template('pacientes.html', pacientes=pacientes)

@app.route('/pacientes/nuevo')
def nuevo_paciente():
    return render_template('paciente_form.html', accion='Nuevo')

@app.route('/consultas')
def listar_consultas():
    return render_template('consultas.html', consultas=consultas)

@app.route('/consultas/nuevo')
def nueva_consulta():
    return render_template('consulta_form.html', accion='Nueva')

@app.route('/maternidad')
def maternidad():
    return render_template('maternidad.html')

@app.route('/chequeo')
def chequeo():
    return render_template('chequeo.html')

@app.route('/emergencia')
def emergencia():
    return render_template('emergencia.html')

if __name__ == '__main__':
    app.run(debug=True)
