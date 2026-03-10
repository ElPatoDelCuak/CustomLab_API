from customlab_models.models import ProductosPersonalizados
from customlab_models.models import Productos
from customlab_models.models import Tallas
from customlab_models.models import ImagenesUsuario

class ProductoPersonalizadoRepository:
    @staticmethod
    def getProductosPersonalizados():
        productos = ProductosPersonalizados.objects.all().order_by('id_producto_personalizado').values(
            'id_producto_personalizado', 'id_producto', 'id_talla', 'id_imagen_usuario', 'color',
            'texto', 'ruta_imagen', 'posicion_xy'
        )
        if not productos.exists():
            return False
        return productos

    @staticmethod
    def getProductoPersonalizadoById(idProductoPersonalizado):
        producto =  ProductosPersonalizados.objects.filter(id_producto_personalizado=idProductoPersonalizado).values(
            'id_producto_personalizado', 'id_producto', 'id_talla', 'id_imagen_usuario', 'color',
            'texto', 'ruta_imagen', 'posicion_xy'        )
        if not producto.exists():
            return False
        return producto

    @staticmethod
    def createProductoPersonalizado(data, ruta_imagen):
        idProducto = Productos.objects.get(id_producto=data.get('id_producto'))
        idTalla = Tallas.objects.get(id_talla=data.get('id_talla'))
        idImagenUsuario = ImagenesUsuario.objects.get(id_imagen_usuario=data.get('id_imagen_usuario'))
        ProductosPersonalizados.objects.create(
            id_producto=idProducto,
            id_talla=idTalla,
            id_imagen_usuario=idImagenUsuario,
            color=data.get('color'),
            texto=data.get('texto'),
            ruta_imagen=ruta_imagen,
            posicion_xy=data.get('posicion_xy'),
        )
        if ProductosPersonalizados.objects.exists():
            return True
        return False

    @staticmethod
    def updateProductoPersonalizado(idProductoPersonalizado, data):
        idProducto = Productos.objects.get(id_producto=data.get('id_producto'))
        idTalla = Tallas.objects.get(id_talla=data.get('id_talla'))
        idImagenUsuario = ImagenesUsuario.objects.get(id_imagen_usuario=data.get('id_imagen_usuario'))
        ProductosPersonalizados.objects.filter(id_producto_personalizado=idProductoPersonalizado).update(
            id_producto_personalizado = idProducto,
            id_talla = idTalla,
            id_imagen_usuario = idImagenUsuario,
            color=data.get('color'),
            texto=data.get('texto'),
            ruta_imagen=data.get('ruta_imagen'),
            posicion_xy=data.get('posicion_xy'),
        )
        if ProductosPersonalizados.objects.filter(id_producto_personalizado=idProductoPersonalizado).exists():
            return True
        return False

    @staticmethod
    def deleteProductoPersonalizado(idProductoPersonalizado):
        ProductosPersonalizados.objects.filter(id_producto_personalizado=idProductoPersonalizado).delete()
        if not ProductosPersonalizados.objects.filter(id_producto_personalizado=idProductoPersonalizado).exists():
            return True
        return False