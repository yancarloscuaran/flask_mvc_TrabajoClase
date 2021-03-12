from src.config.globals as globals

class ProductosModel():
    def traerTodos(self):
        cursor = globals.DB.cursor()

        cursor.execute('select * from productos')

        productos = cursor.fetchall()

        cursor.close()

        return productos

    def crear(self, nombre, descripcion, precio_compra, precio_venta, ganancia, estado):
        cursor = globals.DB.cursor()

        cursor.execute('insert into productos(nombre, descripcion, precio_compra, precio_venta, ganancia, estado) values(?,?,?,?,?,?)', (nombre, descripcion, precio_compra, precio_venta, ganancia, estado,))

        cursor.close()
    

    def editar(self,id, nombre, descripcion, precio_compra, precio_venta, ganancia, estado):

        cursor = globals.DB.cursor()
        cursor.execute('select * from productos where id=?',(id,)).fetchone()
        cursor.execute("""UPDATE productos SET nombre = ?, descripcion = ?, precio_compra= ?, precio_venta= ?, ganancia= ?, estado= ? WHERE id = ?""", (nombre, descripcion, precio_compra, precio_venta, ganancia, estado, id,))

        cursor.close()
