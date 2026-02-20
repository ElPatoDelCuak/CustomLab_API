import os, time
class ImagesService:
    def getImagesImagesByUserId(user_id):
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
    
    def deleteImage(image_id):
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
    
    def saveImage(image, user_id):
        os.makedirs(f'images/{user_id}', exist_ok=True)
        timestamp = int(time.time())
        image_name = f'{user_id}_{image.name}_{timestamp}.jpg'
        image.save(f'images/{user_id}/{image_name}')
        image_path = f'images/{user_id}/{image_name}'
        if os.path.exists(image_path):
            return image_path
        return None