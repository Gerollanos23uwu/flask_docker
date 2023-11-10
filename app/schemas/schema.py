from app import ma 
from marshmallow import fields

class PublicUserSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    nombre_de_usuario = fields.String()

class PrivateUserSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    nombre_de_usuario =fields.String()
    correo_electronico = fields.String()
    password = fields.String()

class PosteosSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    titulo = fields.Integer()
    contenido = fields.Integer()
    fecha_de_creacion = fields.Integer()
    autor_id = fields.Nested(PrivateUserSchema, exclude=['id','password'])
    autor = fields.Integer()


class ComentariosSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    texto = fields.Integer()
    fecha_creacion= fields.Integer()
    autor_id= fields.Integer()
    autor= fields.Integer()        

class CategoriaShema(ma.Schema):
    id = fields.Integer(dump_only=True)
    nombre_etiqueta = fields.Integer    