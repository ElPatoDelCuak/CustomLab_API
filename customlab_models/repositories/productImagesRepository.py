from customlab_models.models import ImagenesProductos

class ProductImagesRepository:
    @staticmethod
    def getProductImagesByProductId(id_producto):
        try:
            images = ImagenesProductos.objects.filter(id_producto_id=id_producto).order_by('id_imagen_producto')
            return [
                {
                    'id_imagen_producto': img.id_imagen_producto,
                    'id_producto': img.id_producto_id,
                    'ruta': img.ruta
                }
                for img in images
            ]
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
    def deleteProductImages(id_producto):
        try:
            ImagenesProductos.objects.filter(id_producto_id=id_producto).delete()
            return True
        except Exception:
            return False