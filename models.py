from extensions import db

class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    dni = db.Column(db.String(8), unique=True, nullable=False)
    telefono = db.Column(db.String(20))
    direccion = db.Column(db.String(120))
    fecha_nacimiento = db.Column(db.String(20))
    genero = db.Column(db.String(10))
    tipo_sangre = db.Column(db.String(5))
    seguro = db.Column(db.String(120))


class Maternidad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    dni = db.Column(db.String(8))
    fecha_control = db.Column(db.String(20))
    edad_gestacional = db.Column(db.Integer)
    presion = db.Column(db.String(20))
    peso = db.Column(db.Float)
    mareos_nauseas = db.Column(db.String(2))  
    alergia = db.Column(db.String(2))         
    detalle_alergia = db.Column(db.Text)
    observaciones = db.Column(db.Text)
    proxima_fecha = db.Column(db.String(20))
    tema = db.Column(db.String(80))


class Chequeo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    dni = db.Column(db.String(20))
    fecha = db.Column(db.String(20))
    temperatura = db.Column(db.String(10))
    presion = db.Column(db.String(20))
    peso = db.Column(db.String(10))
    altura = db.Column(db.String(10))
    medicacion = db.Column(db.String(2))        
    detalle_medicacion = db.Column(db.Text)
    alergia = db.Column(db.String(2))           
    detalle_alergia = db.Column(db.Text)
    observaciones = db.Column(db.Text)


class Emergencia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    dni = db.Column(db.String(8))
    fecha_hora = db.Column(db.String(20))
    tipo = db.Column(db.String(50))
    sangrado = db.Column(db.String(2))     
    alergia = db.Column(db.String(2))       
    detalle_alergia = db.Column(db.Text)
    descripcion_incidente = db.Column(db.Text)
    atencion = db.Column(db.Text)
    referido = db.Column(db.String(120))


class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    especialidad = db.Column(db.String(80))
    turno = db.Column(db.String(20))
    contacto = db.Column(db.String(20))
    correo = db.Column(db.String(120))
    fecha_ingreso = db.Column(db.String(20))
