from customlab_models.models import Productos

class ProductoModel:
    @staticmethod
    def getProductos():
        return Productos.objects.all().values(
            'id_producto', 'precio_venta', 'precio_costo',
            'stock', 'categoria', 'personalizable'
        )

    @staticmethod
    def getProductoById(idProducto):
        return Productos.objects.filter(id_producto=idProducto).values(
            'id_producto', 'precio_venta', 'precio_costo',
            'stock', 'categoria', 'personalizable'
        )