from customlab_models.models import Productos

class ProductoRepository:
    @staticmethod
    def getProductos():
        return Productos.objects.all().values(
            'id_producto', 'nombre_producto', 'precio_venta', 'precio_costo', 
            'stock', 'categoria', 'personalizable'
        )

    @staticmethod
    def getProductoById(idProducto):
        return Productos.objects.filter(id_producto=idProducto).values(
            'id_producto', 'nombre_producto', 'precio_venta', 'precio_costo',
            'stock', 'categoria', 'personalizable'
        )
    
    @staticmethod
    def createProducto(data):
        return Productos.objects.create(
            nombre_producto=data.get('nombre_producto'),
            precio_venta=data.get('precio_venta'),
            precio_costo=data.get('precio_costo'),
            stock=data.get('stock'),
            categoria=data.get('categoria'),
            personalizable=data.get('personalizable'),
        )
    
    @staticmethod
    def updateProducto(idProducto, data):
        Productos.objects.filter(id_producto=idProducto).update(
            nombre_producto=data.get('nombre_producto'),
            precio_venta=data.get('precio_venta'),
            precio_costo=data.get('precio_costo'),
            stock=data.get('stock'),
            categoria=data.get('categoria'),
            personalizable=data.get('personalizable'),
        )
        return Productos.objects.get(id_producto=idProducto)
    
    @staticmethod
    def deleteProducto(idProducto):
        Productos.objects.filter(id_producto=idProducto).delete()