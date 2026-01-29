from .core.models import Productos
class ProductoModel:
    def getProductos():
        return Productos.objects.all().values(
            'id_producto', 'precio_venta', 'precio_costo',
        'stock', 'categoria', 'personalizable'
        )