from customlab_models.repositories.productoRepository import ProductoModel

class ProductoService:
    @staticmethod
    def getProductos():
        productos = ProductoModel.getProductos()
        return list(productos)

    @staticmethod
    def getProductoById(idProducto):
        producto = ProductoModel.getProductoById(idProducto)
        return list(producto)