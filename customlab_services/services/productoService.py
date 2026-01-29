from customlab_models.repositories.productoRepository import ProductoRepository

class ProductoService:
    @staticmethod
    def getProductos():
        productos = ProductoRepository.getProductos()
        return list(productos) or None

    @staticmethod
    def getProductoById(idProducto):
        producto = ProductoRepository.getProductoById(idProducto)
        return list(producto) or None
    
    @staticmethod
    def createProducto(data):
        new_product = ProductoRepository.createProducto(data)
        return {
            'id_producto': new_product.id_producto,
            'nombre_producto': new_product.nombre_producto,
            'precio_venta': new_product.precio_venta,
            'precio_costo': new_product.precio_costo,
            'stock': new_product.stock,
            'categoria': new_product.categoria,
            'personalizable': new_product.personalizable
        }
    
    @staticmethod
    def updateProducto(idProducto, data):
        updated_product = ProductoRepository.updateProducto(idProducto, data)
        if updated_product:
            return {
                'id_producto': updated_product.id_producto,
                'nombre_producto': updated_product.nombre_producto,
                'precio_venta': updated_product.precio_venta,
                'precio_costo': updated_product.precio_costo,
                'stock': updated_product.stock,
                'categoria': updated_product.categoria,
                'personalizable': updated_product.personalizable
            }
        return None
    
    @staticmethod
    def deleteProducto(idProducto):
        producto = ProductoRepository.getProductoById(idProducto)
        if producto:
            ProductoRepository.deleteProducto(idProducto)
            return True
        return False