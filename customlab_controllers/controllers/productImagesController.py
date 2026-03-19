from rest_framework.decorators import api_view
from rest_framework.response import Response
from customlab_services.services.productImagesService import ProductImagesService

@api_view(['GET'])
def getProductImagesByProductId(request, product_id):
    result = ProductImagesService.getProductImagesByProductId(product_id)
    if result['success']:
        for img in result['data']:
            img['ruta'] = request.build_absolute_uri(img['ruta'])
        return Response(result, status=200)
    else:
        return Response(result, status=404)

@api_view(['POST'])
def uploadProductImage(request, product_id):
    images = request.FILES.getlist('images')
    result = ProductImagesService.uploadProductImage(product_id, images)
    if result['success']:
        return Response(result, status=201)
    else:
        return Response(result, status=400)
    
@api_view(['DELETE'])
def deleteProductImage(request, product_id):
    result = ProductImagesService.deleteProductImage(product_id)
    if result['success']:
        return Response(result, status=200)
    else:
        return Response(result, status=400)