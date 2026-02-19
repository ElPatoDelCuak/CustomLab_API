from rest_framework.decorators import api_view
from rest_framework.response import Response
from customlab_services.services.imagesService import imagesService

@api_view(['GET'])
def getImagesByUserId(request, user_id):
    images = imagesService.getImagesByUserId(user_id) 
    if images['success']:
        return Response(images, status=200)
    else:
        return Response(images, status=404)
    
@api_view(['POST'])
def uploadImage(request):
    data = request.data
    result = imagesService.uploadImage(data)
    if result['success']:
        return Response(result, status=201)
    else:
        return Response(result, status=400)
    
@api_view(['DELETE'])
def deleteImage(request, image_id):
    result = imagesService.deleteImage(image_id)
    if result['success']:
        return Response(result, status=200)
    else:
        return Response(result, status=400)