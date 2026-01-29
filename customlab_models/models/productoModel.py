from .core.models import Productos
class ProductoModel:
    def getProductos(self):
        return Productos.objects.all().values(
            'id_producto', 'precio_venta', 'precio_costo',
        'stock', 'categoria', 'personalizable'
        )
    def getProductoById(self, idProducto):
        return Productos.objects.filter(id_producto=idProducto).values(
            'id_producto', 'precio_venta', 'precio_costo',
        'stock', 'categoria', 'personalizable'
        )
    def createProducto(self, data):
        return Productos.objects.create(
            nombre_producto=data[1],
            precio_venta=data[2],
            precio_costo=data[3],
            stock=data[4],
            categoria=data[5],
            personalizable=data[6],
        )
    def updateProducto(self, idProducto, data):
        Productos.objects.filter(id_producto=idProducto).update(
            nombre_producto=data[1],
            precio_venta=data[2],
            precio_costo=data[3],
            stock=data[4],
            categoria=data[5],
            personalizable=data[6],
        )
        return Productos.objects.get(id_producto=idProducto)
    def deleteProducto(self, idProducto):
        Productos.objects.filter(id_producto=idProducto).delete()