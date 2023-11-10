from app import db
from sqlalchemy import ForeignKey

class Usuario(db.Model):
    __tablename__ = "usuario"
    id = db.Column(db.Integer, primary_key=True)
    nombre_de_usuario = db.Column(db.String(100), unique=True, nullable=False)
    correo_electronico = db.Column(db.String(100), unique=True, nullable=False)
    contraseña = db.Column(db.String(100), nullable=False)

class Entrada(db.Model):
    __tablename__ ="entrada"
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    contenido = db.Column(db.Text, nullable=False)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    autor_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    autor = db.relationship('Usuario', backref='entradas')

class Comentario(db.Model):
    __tablename__ ="comentario"
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.Text, nullable=False)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    autor_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    autor = db.relationship('Usuario', backref='comentarios')

class Categoria(db.Model):
    __tablename__ ="categoria"
    id = db.Column(db.Integer, primary_key=True)
    nombre_etiqueta = db.Column(db.String(50), unique=True, nullable=False)
