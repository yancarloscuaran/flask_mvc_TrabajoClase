from flask import render_template
from src import app 
from src.models.productos import ProductosModel

#Refactori reestructurar pero que siga funcionando de igual manera
@app.route('/productos')
def productos():
    productosModel = ProductosModel() #Primer variable debe ser distinta si no genera error.
    

    productos = productosModel.traerTodos()


    return render_template('productos/index.html', productos = productos)