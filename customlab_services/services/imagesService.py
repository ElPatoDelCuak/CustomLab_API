import os, time
from django.conf import settings

BASE_IMAGES_DIR = os.path.join(settings.MEDIA_ROOT, 'images')

class ImagesService:
    
    @staticmethod
    def saveImage(image, id, upload_type):
        if upload_type == 1:
            dir = os.path.join(settings.MEDIA_ROOT, 'images', 'users', str(id))
            dir_name = 'users'
        if upload_type == 2:
            dir = os.path.join(settings.MEDIA_ROOT, 'images', 'personalizable_clothes', str(id))
            dir_name = 'personalizable_clothes'
        if upload_type == 3:
            dir = os.path.join(settings.MEDIA_ROOT, 'images', 'products', str(id))
            dir_name = 'products'

        os.makedirs(dir, exist_ok=True)

        timestamp = int(time.time())
        image_name = f'{id}_{image.name}_{timestamp}.jpg'
        image_path = os.path.join(dir, image_name)

        with open(image_path, 'wb+') as f:
            for chunk in image.chunks():
                f.write(chunk)

        if os.path.exists(image_path):
            image_url = f'{settings.MEDIA_URL}images/{dir_name}/{id}/{image_name}'
            return image_url
        return None
    
    @staticmethod
    def deleteImage(image_path):
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