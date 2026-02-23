from customlab_models.repositories.userImagesRepository import UserImagesRepository
from customlab_services.services.imagesService import ImagesService

class UserImagesService:

    @staticmethod
    def getImageById(image_id):
        image = UserImagesRepository.getImageById(image_id)
        if image:
            return {'success': True, 'data': image}
        return {'success': False, 'message': 'Image not found'}

    @staticmethod
    def getImagesByUserId(user_id):
        images = UserImagesRepository.getImagesByUserId(user_id)
        if images:
            return {'success': True, 'data': images}
        return {'success': False, 'message': 'No images found for this user'}
    
    @staticmethod
    def uploadImage(data):
        image = data.get('image')
        user_id = data.get('user_id')
        upload_type = data.get('upload_type')

        if not image or not user_id:
            return {'success': False, 'message': 'Image and user_id are required'}

        if not ImagesService.verifyImage(image):
            return {'success': False, 'message': 'Invalid image format'}

        image_path = ImagesService.saveImage(image, user_id, upload_type)
        if not image_path:
            return {'success': False, 'message': 'Error saving image'}
        
        data['image_path'] = image_path
        success = UserImagesRepository.uploadImagePath(data)

        if success:
            return {'success': True, 'message': 'Image uploaded successfully'}
        return {'success': False, 'message': 'Error uploading image'}
    
    @staticmethod
    def deleteImage(image_id):
        image = UserImagesService.getImageById(image_id)
        if not image['success']:
            return image
        
        file_deleted = ImagesService.deleteImage(image['data']['ruta'])
        if not file_deleted:
            return {'success': False, 'message': 'Error deleting image file'}

        success = UserImagesRepository.deleteImage(image_id)
        if success:
            return {'success': True, 'message': 'Image deleted successfully'}
        return {'success': False, 'message': 'Error deleting image'}