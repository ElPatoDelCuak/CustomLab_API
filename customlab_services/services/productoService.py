from customlab_models.repositories.productoRepository import ProductoRepository

class ProductoService:
    @staticmethod
    def getProductos():
        productos = ProductoRepository.getProductos()
        return list(productos)

    @staticmethod
    def getProductoById(idProducto):
        producto = ProductoRepository.getProductoById(idProducto)
        return list(producto)