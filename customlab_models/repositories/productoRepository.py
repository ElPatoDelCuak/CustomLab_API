from customlab_models.models import Productos

class ProductoRepository:
    @staticmethod
    def getProductos():
        return Productos.objects.all().order_by('id_producto').values(
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
        Productos.objects.create(
            nombre_producto=data.get('nombre_producto'),
            precio_venta=data.get('precio_venta'),
            precio_costo=data.get('precio_costo'),
            stock=data.get('stock'),
            categoria=data.get('categoria'),
            personalizable=data.get('personalizable'),
        )
        if Productos.objects.exists():
            return True
        return False
    
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
        if Productos.objects.filter(id_producto=idProducto).exists():
            return True
        return False
    
    @staticmethod
    def deleteProducto(idProducto):
        Productos.objects.filter(id_producto=idProducto).delete()
        if not Productos.objects.filter(id_producto=idProducto).exists():
            return True
        return False