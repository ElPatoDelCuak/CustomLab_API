import os, time

BASE_IMAGES_DIR = 'images'
class ImagesService:

    @staticmethod
    def getImagesByUserId(user_id):
        images = ImagesRepository.getImagesByUserId(user_id)
        if images:
            return {
                'success': True,
                'data': images
            }
        return {
            'success': False,
            'message': 'No images found for this user'
        }
    
    @staticmethod
    def uploadImage(data):
        image = data.get('image')
        user_id = data.get('user_id')
        if not image or not user_id:
            return {
                'success': False,
                'message': 'Image and user_id are required'
            }
        image_path = ImagesService.saveImage(image, user_id)
        if not image_path:
            return {
                'success': False,
                'message': 'Error saving image'
            }
        
        data['image_path'] = image_path
        success = ImagesRepository.uploadImage(data)
        if success:
            return {
                'success': True,
                'message': 'Image uploaded successfully'
            }
        return {
            'success': False,
            'message': 'Error uploading image'
        }
    
    @staticmethod
    def deleteImage(image_id):
        image = ImagesRepository.getImageById(image_id)
        if not image:
            return {
                'success': False,
                'message': 'Image not found'
            }
        image_path = image['image_path']
        file_deleted = ImagesService.deleteImageFile(image_path)
        if not file_deleted:
            return {
                'success': False,
                'message': 'Error deleting image file'
            }
        success = ImagesRepository.deleteImage(image_id)
        if success:
            return {
                'success': True,
                'message': 'Image deleted successfully'
            }
        return {
            'success': False,
            'message': 'Error deleting image'
        }
    
    @staticmethod
    def saveImage(image, user_id):
        os.makedirs(f'{BASE_IMAGES_DIR}/{user_id}', exist_ok=True)
        timestamp = int(time.time())
        image_name = f'{user_id}_{image.name}_{timestamp}.jpg'
        image.save(f'{BASE_IMAGES_DIR}/{user_id}/{image_name}')
        image_path = f'{BASE_IMAGES_DIR}/{user_id}/{image_name}'
        if os.path.exists(image_path):
            return image_path
        return None
    
    @staticmethod
    def deleteImageFile(image_path):
        if os.path.exists(image_path):
            os.remove(image_path)
            return True
        return False