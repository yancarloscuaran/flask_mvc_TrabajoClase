from flask import render_template, request, redirect, url_for
from src import app 
from src.models.productos import ProductosModel

#Refactori reestructurar pero que siga funcionando de igual manera
@app.route('/productos')
def productos():
    productosModel = ProductosModel() #Primer variable debe ser distinta si no genera error.
    

    productos = productosModel.traerTodos()


    return render_template('productos/index.html', productos = productos)

@app.route('/productos/crear', methods=['GET', 'POST'])
def crear_producto():
    #Esta funcion me sirve para mostrar el formulario de creacion 
    #y tambien me sirve para crear un nuevo producto
    # Estos pasos se identifican con los metodos
    if request.method == 'GET':
        # Mostramos el formulario de creacion
        return render_template('productos/crear.html')
    
    # es la creacion del producto
    nombre= request.form.get('nombre')

    descripcion= request.form.get('descripcion')

    precio_compra= request.form.get('precio_compra')

    precio_venta= request.form.get('precio_venta')

    ganancia= request.form.get('ganancia')

    estado= request.form.get('estado')

    productosModel = ProductosModel()

    productosModel.crear(nombre, descripcion, precio_compra, precio_venta, ganancia,estado)
    return redirect(url_for('productos'))

@app.route('/productos/editar/<int:id>', methods=('GET', 'POST'))
def actualizar_producto(id):
    if request.method == 'GET':
        
        return render_template('productos/editar.html')

    nombre= request.form.get('nombre')
    descripcion= request.form.get('descripcion')
    precio_compra= request.form.get('precio_compra')
    precio_venta= request.form.get('precio_venta')
    ganancia= request.form.get('ganancia')
    estado= request.form.get('estado')

    productosModel = ProductosModel()
    
    productosModel.editar(id,nombre, descripcion, precio_compra, precio_venta, ganancia,estado)
    
    return redirect(url_for('productos'))

