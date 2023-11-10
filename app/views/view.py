from flask import jsonify, request

from flask.views import MethodView

from flask import(
    Flask,
    request,
)




from flask_jwt_extended import(
    create_access_token,
    get_jwt,
    get_jwt_identity,
    jwt_required
)
from app import app,db

from app.schemas.schema import PosteosSchema, PrivateUserSchema, PublicUserSchema, CategoriaShema
from app.models.models import Usuario, Entrada, Categoria, Comentario

# Ruta para la página de inicio
@app.route('/')
def index():
    return jsonify(index="Api_funciondo")

# Ruta para ver la lista de usuarios
class MetodoUsuario(MethodView):
    def get(self):
        all_users = Usuario.query.all()
        user_schema = PublicUserSchema().dump(all_users, many=True)
        return jsonify(user_schema)
    
    def post(self):
        # Obtener los datos ingresados en el formulario
        data = request.get_json()
        nombre = data.get('nombre')
        correo_electronico = data.get('correo_electronico')
        contraseña = data.get('contraseña')


        # Crear un nuevo usuario y guardar los datos en la base de datos
        new_user = Usuario(nombre_de_usuario=nombre, correo_electronico=correo_electronico, contraseña=contraseña)
        db.session.add(new_user)
        db.session.commit()

        return jsonify(Crear="User creado"), 201
    
app.add_url_rule("/users", view_func=MetodoUsuario.as_view("Usuarios"))
        
class MetodoEnrada(MethodView):
    def get (self):
        add_posts = Entrada.query.all()
        post_schema = PosteosSchema().dump(add_posts, many=True)
        return jsonify (post_schema), 200
    
    def post(self):
        post = request.get_json()
        titulo = post.get('titulo')
        contenido  = post.get('contenido')
        fecha_creacion = post.get('fecha_creacion')
        autor_id=post.get('autor')

        new_post = Entrada(titulo = titulo, contenido=contenido, fecha_creacion=fecha_creacion, autor_id=autor_id)
        db.session.add(new_post)
        db.session.commit()

        return jsonify(crear="posteo crado"), 201
    
    def delete(self, post_id):
        post = Entrada.query.get(post_id)

        db.session.delete(post)
        db.session.commit()
        return jsonify(Mensaje=f"User {post_id} deleted"), 301

class MetodoCategoria(MethodView):
    def get(self):
        all_categoria = Categoria.query.all()
        categoria_shema = CategoriaShema().dump(all_categoria, many=True)
        return jsonify(categoria_shema), 201
    

    def post(self):
        categoria=request.get_json()
        nombre_etiqueta = categoria.get("nombre_etiqueta")
        id=categoria.get("id")
        print("medio")
        new_categoria = Categoria(nombre_etiqueta=nombre_etiqueta, id=id)
        db.session.add(new_categoria)
        db.session.commit()

        return jsonify(crear="categoria_creada"), 201
    
app.add_url_rule("/add_post", view_func=MetodoEnrada.as_view("Posteos"))
app.add_url_rule("/add_post/<post_id>", view_func=MetodoEnrada.as_view("Borrar_posteo"))
app.add_url_rule("/add_categoria", view_func=MetodoCategoria.as_view("Categoria"))