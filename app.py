from flask import Flask, render_template, redirect, url_for, flash, request, session
import os
from functools import wraps
from extensions import db
from werkzeug.security import check_password_hash
from models import Usuario, Paciente, Maternidad, Chequeo, Emergencia, Doctor

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'clave-demo')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinica.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


# ---------------- LOGIN -----------------
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        usuario_input = request.form['usuario']
        password_input = request.form['password']
        sucursal = request.form['sucursal']

        usuario = Usuario.query.filter_by(usuario=usuario_input).first()

        # CORREGIDO: tu modelo usa self.password, no password_hash
        if usuario and usuario.check_password(password_input):
            session['usuario'] = usuario.usuario
            session['sucursal'] = usuario.sucursal
            return redirect('/inicio')
        else:
            error = "Usuario o contraseña incorrectos"

    return render_template('login.html', error=error)


# ---------------- PROTECCIÓN DE RUTAS -----------------
def login_required(f):
    @wraps(f)     # <- SOLUCIÓN DEL ERROR
    def wrapper(*args, **kwargs):
        if 'usuario' not in session:
            return redirect('/')
        return f(*args, **kwargs)
    return wrapper


# ---------------- USUARIOS -----------------
@app.route('/usuarios/nuevo', methods=['GET', 'POST'])
@login_required
def nuevo_usuario():

    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        sucursal = request.form['sucursal']

        existente = Usuario.query.filter_by(usuario=usuario).first()
        if existente:
            flash("❌ El usuario ya existe", "danger")
            return redirect(url_for('nuevo_usuario'))

        nuevo = Usuario(
            usuario=usuario,
            sucursal=sucursal
        )
        nuevo.set_password(password)

        db.session.add(nuevo)
        db.session.commit()

        flash("✔ Usuario creado correctamente", "success")
        return redirect('/inicio')

    return render_template('usuario_form.html')


# ---------------- INICIO -----------------
@app.route('/inicio')
@login_required
def inicio():
    return render_template('index.html')


# ---------------- LOGOUT -----------------
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


# ---------------- PACIENTES -----------------
@app.route('/pacientes')
@login_required
def listar_pacientes():
    pacientes = Paciente.query.all()
    return render_template('pacientes.html', pacientes=pacientes)


@app.route('/pacientes/nuevo', methods=['GET', 'POST'])
@login_required
def nuevo_paciente():
    if request.method == 'POST':
        nuevo = Paciente(
            nombre=request.form['nombre'],
            dni=request.form['dni'],
            telefono=request.form['telefono'],
            direccion=request.form['direccion'],
            fecha_nacimiento=request.form['fecha_nacimiento'],
            genero=request.form['genero'],
            tipo_sangre=request.form['tipo_sangre'],
            seguro=request.form['seguro'],
        )

        db.session.add(nuevo)
        db.session.commit()
        return redirect('/pacientes')

    return render_template('paciente_form.html', accion="Nuevo")


# ---------------- MATERNIDAD -----------------
@app.route('/maternidad')
@login_required
def listar_maternidad():
    registros = Maternidad.query.all()
    return render_template('maternidad.html', maternidad=registros)


@app.route('/maternidad/nuevo', methods=['GET', 'POST'])
@login_required
def nueva_maternidad():
    if request.method == 'POST':
        nueva = Maternidad(
            nombre=request.form['nombre'],
            dni=request.form['dni'],
            fecha_control=request.form['fecha_control'],
            edad_gestacional=request.form['edad_gestacional'],
            presion=request.form['presion'],
            peso=request.form['peso'],
            mareos_nauseas=request.form['mareos_nauseas'],
            alergia=request.form['alergia'],
            detalle_alergia=request.form['detalle_alergia'],
            observaciones=request.form['observaciones'],
            proxima_fecha=request.form['proxima_fecha'],
            tema=request.form['tema']
        )

        db.session.add(nueva)
        db.session.commit()

        return redirect('/maternidad')

    return render_template('maternidad_form.html', accion="Nuevo")


# ---------------- CHEQUEO -----------------
@app.route('/chequeo')
@login_required
def listar_chequeo():
    registros = Chequeo.query.all()
    return render_template('chequeo.html', chequeo=registros)


@app.route('/chequeo/nuevo', methods=['GET', 'POST'])
@login_required
def nuevo_chequeo():
    if request.method == 'POST':
        nuevo = Chequeo(
            nombre=request.form['nombre'],
            dni=request.form['dni'],
            fecha=request.form['fecha'],
            temperatura=request.form['temperatura'],
            presion=request.form['presion'],
            peso=request.form['peso'],
            altura=request.form['altura'],
            medicacion=request.form['medicacion'],
            detalle_medicacion=request.form.get('detalle_medicacion', ''),
            alergia=request.form['alergia'],
            detalle_alergia=request.form.get('detalle_alergia', ''),
            observaciones=request.form['observaciones']
        )

        db.session.add(nuevo)
        db.session.commit()

        return redirect('/chequeo')

    return render_template('chequeo_form.html', accion="Nuevo")


# ---------------- EMERGENCIA -----------------
@app.route('/emergencia')
@login_required
def listar_emergencia():
    registros = Emergencia.query.all()
    return render_template('emergencia.html', emergencia=registros)


@app.route('/emergencia/nuevo', methods=['GET', 'POST'])
@login_required
def nueva_emergencia():
    if request.method == 'POST':
        nueva = Emergencia(
            nombre=request.form['nombre'],
            dni=request.form['dni'],
            fecha_hora=request.form['fecha_hora'],
            tipo=request.form['tipo'],
            sangrado=request.form['sangrado'],
            alergia=request.form['alergia'],
            detalle_alergia=request.form['detalle_alergia'],
            descripcion_incidente=request.form['descripcion_incidente'],
            atencion=request.form['atencion'],
            referido=request.form['referido']
        )

        db.session.add(nueva)
        db.session.commit()

        return redirect('/emergencia')

    return render_template('emergencia_form.html', accion="Nuevo")


# ---------------- DOCTORES -----------------
@app.route('/doctores')
@login_required
def listar_doctores():
    registros = Doctor.query.all()
    return render_template('doctores.html', doctores=registros)


@app.route('/doctores/nuevo', methods=['GET', 'POST'])
@login_required
def nuevo_doctor():
    if request.method == 'POST':
        nuevo = Doctor(
            nombre=request.form['nombre'],
            especialidad=request.form['especialidad'],
            turno=request.form['turno'],
            contacto=request.form['contacto'],
            correo=request.form['correo'],
            fecha_ingreso=request.form['fecha_ingreso'],
        )

        db.session.add(nuevo)
        db.session.commit()

        return redirect('/doctores')

    return render_template('doctores_form.html', accion="Nuevo")


# ---------------- DASHBOARD -----------------
@app.route('/dashboard')
@login_required
def dashboard():
    tipos_emergencia = {}
    for e in Emergencia.query.all():
        tipos_emergencia[e.tipo] = tipos_emergencia.get(e.tipo, 0) + 1

    chequeos_por_persona = {}
    for c in Chequeo.query.all():
        chequeos_por_persona[c.nombre] = chequeos_por_persona.get(c.nombre, 0) + 1

    especialidades = {}
    for d in Doctor.query.all():
        especialidades[d.especialidad] = especialidades.get(d.especialidad, 0) + 1

    import datetime
    hoy = datetime.date.today()

    joven = adulto = adulto_mayor = 0
    for p in Paciente.query.all():
        try:
            año, mes, dia = map(int, p.fecha_nacimiento.split("-"))
            edad = hoy.year - año
            if edad < 30:
                joven += 1
            elif edad < 60:
                adulto += 1
            else:
                adulto_mayor += 1
        except:
            pass

    return render_template(
        "dashboard.html",
        tipos_emergencia=tipos_emergencia,
        chequeos_por_persona=chequeos_por_persona,
        especialidades=especialidades,
        joven=joven,
        adulto=adulto,
        adulto_mayor=adulto_mayor
    )


if __name__ == '__main__':
    app.run(debug=True)

import commands
commands.init_app(app)