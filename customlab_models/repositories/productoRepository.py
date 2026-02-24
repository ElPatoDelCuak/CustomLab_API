from customlab_models.models import Productos
from customlab_models.models import ImagenesProductos

class ProductoRepository:
    @staticmethod
    def getProductos():
        productos = Productos.objects.all().order_by('id_producto').values(
            'id_producto', 'nombre_producto', 'precio_venta', 'precio_costo',
            'stock', 'categoria', 'personalizable'
        )
        if not productos.exists():
            return False
        return list(productos)

    @staticmethod
    def getProductoById(idProducto):
        producto = Productos.objects.filter(id_producto=idProducto).values(
            'id_producto', 'nombre_producto', 'precio_venta', 'precio_costo',
            'stock', 'categoria', 'personalizable'
        ).first()
        return producto or None

    @staticmethod
    def getProductImages(idProducto):
        return list(
            ImagenesProductos.objects.filter(id_producto_id=idProducto)
            .values('id_imagen_producto', 'ruta')
        )

    @staticmethod
    def deleteProductImages(idProducto):
        ImagenesProductos.objects.filter(id_producto_id=idProducto).delete()
        return True
    
    @staticmethod
    def createProducto(data):
        try:
            producto = Productos.objects.create(
                nombre_producto=data.get('nombre_producto'),
                precio_venta=data.get('precio_venta'),
                precio_costo=data.get('precio_costo'),
                stock=data.get('stock'),
                categoria=data.get('categoria'),
                personalizable=data.get('personalizable'),
            )
            return producto
        except Exception:
            return None
    
    @staticmethod
    def saveProductImages(id_producto, image_path):
        try:
            ImagenesProductos.objects.create(
                id_producto_id=id_producto,
                ruta=image_path
            )
            return True
        except Exception:
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
        return not Productos.objects.filter(id_producto=idProducto).exists()