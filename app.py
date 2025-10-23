from flask import Flask, render_template, redirect, url_for, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave-demo'

pacientes = [
    {"id": 1, "nombre": "Pedro Gomez", "dni": "12345678", "telefono": "987654321"},
    {"id": 2, "nombre": "Adriana Tenorio", "dni": "87654321", "telefono": "912345678"},
]

consultas = [
    {"id": 1, "paciente": "Pedro Gomez", "motivo": "Dolor de cabeza", "fecha": "2025-10-20"},
    {"id": 2, "paciente": "Adriana Tenorio", "motivo": "Chequeo general", "fecha": "2025-10-21"},
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

if __name__ == '__main__':
    app.run(debug=True)
