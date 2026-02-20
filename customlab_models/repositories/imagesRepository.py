from customlab_models.models import ImagenesUsuario

class ImagesRepository:
    
    @staticmethod
    def getImageById(image_id):
        image = ImagenesUsuario.objects.filter(id_imagen_usuario=image_id).values('id_imagen_usuario', 'ruta')
        if not image.exists():
            return False
        return image.first()

    @staticmethod
    def getImagesByUserId(user_id):
        images = ImagenesUsuario.objects.filter(id_usuario=user_id).values('id_imagen_usuario', 'ruta')
        if not images.exists():
            return False
        return images
    
    @staticmethod
    def uploadImage(data):
        image = ImagenesUsuario.objects.create(
            id_usuario_id=data.get('user_id'),
            ruta=data.get('image_path')
        )
        image_exist = ImagenesUsuario.objects.filter(id_imagen_usuario=image.id_imagen_usuario).exists()
        if image_exist:
            return True
        return False

    @staticmethod
    def deleteImage(image_id):
        ImagenesUsuario.objects.filter(id_imagen_usuario=image_id).delete()
        if not ImagenesUsuario.objects.filter(id_imagen_usuario=image_id).exists():
            return True
        return False