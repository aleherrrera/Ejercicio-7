from __main__ import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Usuarios(db.Model):
    DNI = db.Column(db.String, primary_key=True)
    Clave = db.Column(db.String(120), nullable=False, unique=True)
    Tipo = db.Column(db.String(10), nullable= False)
    pedido = db.relationship('Pedidos', backref='usuarios', cascade="all, delete-orphan", lazy='dynamic')

class Pedidos(db.Model):
    __tablename__= 'Pedidos'
    NumPedido = db.Column(db.Integer, primary_key=True)
    Fecha = db.Column(db.DateTime)
    Total = db.Column(db.Integer, nullable=False)
    Cobrado = db.Column(db.Boolean, unique=False, default=False)
    Observacion = db.Column(db.Text, default=None)
    Mesa = db.Column(db.Integer, unique=True, nullable=False)
    DNIMozo = db.Column(db.String, db.ForeignKey('usuarios.DNI'))
    items_pedidos = db.relationship('ItemsPedidos', backref='pedidos', cascade="all, delete-orphan", lazy='dynamic')

class ItemsPedidos(db.Model):
    __tablename__= 'ItemsPedidos'
    NumItem = db.Column(db.Integer, primary_key=True)
    NumPedido = db.Column(db.Integer, db.ForeignKey('Pedidos.NumPedido'))
    NumProducto = db.Column(db.Integer, db.ForeignKey('productos.NumProducto'))
    Precio = db.Column(db.Integer, nullable=False)
    Estado = db.Column(db.String(10), nullable=False)

class Productos(db.Model):
    NumProducto = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(20), unique=True, nullable=False)
    PrecioUnitario = db.Column(db.Integer, nullable=False)
    num_item = db.relationship('ItemsPedidos', backref='productos', cascade="all, delete-orphan", lazy='dynamic')
