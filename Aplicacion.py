import hashlib
import datetime
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config.from_pyfile('config.py')

from modelos import db
from modelos import Usuarios, Pedidos, Productos, ItemsPedidos


@app.route('/', methods=['GET', 'POST'])
def ingreso_usuario():
    if request.method == 'POST':
        if not request.form['password'] or not request.form['dni']:
            return render_template('error.html', error="Por favor ingrese los datos requeridos")
        else:
            usuario_actual = Usuarios.query.filter_by(DNI=request.form['dni']).first()
            if usuario_actual is None:
                return render_template('error.html', error="El usuario no está registrado")
            else:
                clave = request.form['password']
                result = hashlib.md5(bytes(clave, encoding='utf-8'))
                if usuario_actual.Clave != result.hexdigest():
                    return render_template('error.html', error="La contraseña no es válida")
                else:
                    if usuario_actual.Tipo=='Mozo':
                        return render_template('funciones_mozo.html', usuario=usuario_actual)
                    else:
                        if usuario_actual.Tipo=='Cocinero':
                            return render_template('funciones_cocinero.html', usuario=usuario_actual)
                        else:
                            return render_template('error.html', error='El tipo ingresado es incorrecto')
    else:
        return render_template('ingreso_usuario.html')

@app.route('/funciones_mozo')
def funciones_mozo():
    return render_template('funciones_mozo.html')

@app.route('/crear_pedido', methods=['GET', 'POST'])
def crear_pedido():
    if request.method == 'POST':
        if not request.form['mesa']:
            return render_template('error_2.html', error='Ingrese numero de mesa')
        else:
            pedido_actual=Pedidos.query.filter_by(Mesa=request.form['mesa']).first()

            if pedido_actual is None or pedido_actual.Cobrado is True:
                d = (Pedidos.query.count()) + 2
                mozo = Usuarios.query.filter_by(Tipo='Mozo').first()
                pedido_new = Pedidos(NumPedido=d, Fecha=datetime.date.today(), Total=0, Mesa=request.form['mesa'],
                                     DNIMozo=mozo.DNI)
                db.session.add(pedido_new)
                db.session.commit()
                return render_template('menu.html', productos=Productos.query.all(), pedido=None, items=None,
                                       mesa=request.form['mesa'])
            else:
                items_actuales = ItemsPedidos.query.filter_by(NumPedido=pedido_actual.NumPedido).all()
                return render_template('menu.html', productos=Productos.query.all(), pedido=pedido_actual,
                                       mesa=request.form['mesa'], items=items_actuales)
    else:
        return render_template('crear_pedido.html')

@app.route('/menu', methods=['GET', 'POST'])
def menu():
    if request.method == 'POST':
        if not request.form['mesa']:
            return render_template('error_2.html', error='Ingrese numero de mesa')
        else:
            pedido_actual = Pedidos.query.filter_by(Mesa=request.form['mesa']).first()
            if pedido_actual is None:
                return render_template('crear_pedido.html')
            else:
                producto= Productos.query.filter_by(Nombre=request.form['producto']).first()
                c=(ItemsPedidos.query.count())+2
                new_item= ItemsPedidos(NumItem=c, NumPedido=pedido_actual.NumPedido, NumProducto=producto.NumProducto,
                                         Precio=producto.PrecioUnitario, Estado='Pendiente')
                db.session.add(new_item)
                db.session.commit()
                pedido_actual.Total=int(new_item.Precio)+int(pedido_actual.Total)
                db.session.add(pedido_actual)
                db.session.commit()
                items_actuales = ItemsPedidos.query.filter_by(NumPedido=pedido_actual.NumPedido).all()
                return render_template('menu.html', productos=Productos.query.all(), pedido=pedido_actual,
                                    mesa=request.form['mesa'],items=items_actuales)
    else:
        return render_template('crear_pedido.html')

@app.route('/cerrar_pedido', methods=['GET', 'POST'])
def cerrar_pedido():
    if request.method == 'POST':
        if not request.form['pedido']:
            return render_template('error_2.html', error='Error numero de pedido')
        else:
            pedido_new= Pedidos.query.filter_by(NumPedido=int(request.form['pedido'])).first()
            if request.form['observacion'] is None:
                db.session.add(pedido_new)
                db.session.commit()
            else:
                pedido_new.Observacion=request.form['observacion']
                db.session.add(pedido_new)
                db.session.commit()
            return render_template('funciones_mozo.html')
    else:
        return render_template('crear_pedido.html')

@app.route('/listar_pedidos_vigentes', methods=['GET', 'POST'])
def listar_pedidos_vigentes():
    if request.method != 'POST':
        hoy = str(datetime.date.today())
        lista=[]
        p = Pedidos.query.filter_by(Cobrado=False).all()
        for pedido in p:
            fecha=str(pedido.Fecha)
            partes = fecha.split(" ")[0].split("-")
            new_fecha = "-".join((partes))
            if new_fecha == hoy:
                lista.append(pedido)

        return render_template('listar_pedidos_vigentes.html',pedidos=lista
                               ,items=ItemsPedidos.query.all())

@app.route('/registrar_cobro', methods=['GET', 'POST'])
def registrar_cobro():
    if request.method == 'POST':
        if request.form['pedido'] is None:
            return render_template('funciones_mozo.html')
        else:
            pedido = Pedidos.query.filter_by(NumPedido=int(request.form['pedido'])).first()
            pedido.Cobrado=True
            db.session.add(pedido)
            db.session.commit()

            hoy = str(datetime.date.today())
            lista = []
            p = Pedidos.query.filter_by(Cobrado=False).all()
            for pedido in p:
                fecha = str(pedido.Fecha)
                partes = fecha.split(" ")[0].split("-")
                new_fecha = "-".join((partes))
                if new_fecha == hoy:
                    lista.append(pedido)
            return render_template('listar_pedidos_vigentes.html',pedidos=lista
                               ,items=ItemsPedidos.query.all())
    else:
        return render_template('funciones_mozo.html')

@app.route('/funciones_cocinero')
def funciones_cocinero():
    return render_template('funciones_cocinero.html')

@app.route('/item_listo', methods=['GET', 'POST'])
def item_listo():
    if request.method == 'POST':
        if not request.form['item']:
            return render_template('funciones_cocinero.html')
        else:
            it_listo= ItemsPedidos.query.filter_by(NumItem=request.form['item']).first()
            it_listo.Estado='Listo'
            db.session.add(it_listo)
            db.session.commit()
            items = ItemsPedidos.query.filter_by(Estado='Pendiente').all()
            a=0
            lista = []
            for item in items:
                if item.pedidos.NumPedido != a:
                    a = item.pedidos.NumPedido
                    lista.append(item.pedidos.NumPedido)
            return render_template('item_listo.html', items=items, pedidos=lista)
    else:
        items = ItemsPedidos.query.filter_by(Estado='Pendiente').all()
        a = 0
        lista=[]
        for item in items:
            if item.pedidos.NumPedido != a:
                a=item.pedidos.NumPedido
                lista.append(item.pedidos.NumPedido)
        return render_template('item_listo.html',items=items,pedidos=lista)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)