import os, time
from customlab_models.repositories.imagesRepository import ImagesRepository
from django.conf import settings

BASE_IMAGES_DIR = os.path.join(settings.MEDIA_ROOT, 'images')

class ImagesService:

    @staticmethod
    def getImageById(image_id):
        image = ImagesRepository.getImageById(image_id)
        if image:
            return {'success': True, 'data': image}
        return {'success': False, 'message': 'Image not found'}

    @staticmethod
    def getImagesByUserId(user_id):
        images = ImagesRepository.getImagesByUserId(user_id)
        if images:
            return {'success': True, 'data': images}
        return {'success': False, 'message': 'No images found for this user'}
    
    @staticmethod
    def uploadImage(data):
        image = data.get('image')
        user_id = data.get('user_id')

        if not image or not user_id:
            return {'success': False, 'message': 'Image and user_id are required'}

        if not ImagesService.verifyImage(image):
            return {'success': False, 'message': 'Invalid image format'}

        image_path = ImagesService.saveImage(image, user_id)
        if not image_path:
            return {'success': False, 'message': 'Error saving image'}
        
        data['image_path'] = image_path
        success = ImagesRepository.uploadImage(data)

        if success:
            return {'success': True, 'message': 'Image uploaded successfully'}
        return {'success': False, 'message': 'Error uploading image'}
    
    @staticmethod
    def deleteImage(image_id):
        image = ImagesService.getImageById(image_id)
        if not image['success']:
            return image
        
        file_deleted = ImagesService.deleteImageFile(image['data']['ruta'])
        if not file_deleted:
            return {'success': False, 'message': 'Error deleting image file'}

        success = ImagesRepository.deleteImage(image_id)
        if success:
            return {'success': True, 'message': 'Image deleted successfully'}
        return {'success': False, 'message': 'Error deleting image'}
    
    @staticmethod
    def saveImage(image, user_id):
        user_dir = os.path.join(settings.MEDIA_ROOT, 'images', 'users', str(user_id))
        os.makedirs(user_dir, exist_ok=True)

        timestamp = int(time.time())
        image_name = f'{user_id}_{image.name}_{timestamp}.jpg'
        image_path = os.path.join(user_dir, image_name)

        with open(image_path, 'wb+') as f:
            for chunk in image.chunks():
                f.write(chunk)

        if os.path.exists(image_path):
            image_url = f'{settings.MEDIA_URL}images/users/{user_id}/{image_name}'
            return image_url
        return None
    
    @staticmethod
    def deleteImageFile(image_path):
        file_path = image_path
        if image_path.startswith(settings.MEDIA_URL):
            relative_path = image_path.replace(settings.MEDIA_URL, '', 1)
            file_path = os.path.join(settings.MEDIA_ROOT, relative_path)
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        return False
    
    @staticmethod
    def verifyImage(image):
        allowed_extensions = ['jpg', 'jpeg', 'png']
        extension = image.name.split('.')[-1].lower()
        return extension in allowed_extensions