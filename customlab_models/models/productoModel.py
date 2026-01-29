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