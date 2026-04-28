from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from customlab_services.services.productoService import ProductoService
from customlab_api.permissions import IsAdminOrManager

@api_view(['GET'])
@permission_classes([AllowAny])
def getProductos(request):
    productos = ProductoService.getProductos()
    if productos['success']:
        for producto in productos['data']:
            for img in producto.get('images', []):
                img['ruta'] = request.build_absolute_uri(img['ruta'])
        return Response(productos, status=200)
    else:
        return Response(productos, status=404)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProductoById(request, id):
    producto = ProductoService.getProductoById(id)
    if producto['success']:
        for img in producto['data'].get('images', []):
            img['ruta'] = request.build_absolute_uri(img['ruta'])
        return Response(producto, status=200)
    else:
        return Response(producto, status=404)

@api_view(['GET'])
@permission_classes([AllowAny])
def getFeaturedProducts(request):
    productos = ProductoService.getFeaturedProducts()
    if productos['success']:
        for producto in productos['data']:
            for img in producto.get('images', []):
                img['ruta'] = request.build_absolute_uri(img['ruta'])
        return Response(productos, status=200)
    else:
        return Response(productos, status=404)

@api_view(['POST'])
@permission_classes([IsAdminOrManager])
def createProducto(request):
    data = request.data
    images = request.FILES.getlist('images') or request.FILES.getlist('images[]')
    result = ProductoService.createProducto(data, images)
    if result['success']:
        return Response(result, status=201)
    else:
        return Response(result, status=400)

@api_view(['PATCH'])
@permission_classes([IsAdminOrManager])
def updateProducto(request, id):
    # El JSON estructurado vendrá en el campo 'data' del FormData
    json_data = request.data.get('data')
    # Las imágenes nuevas vendrán en el campo 'new_images'
    new_images = request.FILES.getlist('new_images') or request.FILES.getlist('new_images[]')
    
    if not json_data:
        return Response({
            'success': False,
            'message': 'Se requiere el campo "data" con la configuración JSON'
        }, status=400)

    result = ProductoService.updateProducto(id, json_data, new_images)
    if result['success']:
        return Response(result, status=200)
    else:
        return Response(result, status=400)

@api_view(['DELETE'])
@permission_classes([IsAdminOrManager])
def deleteProducto(request, id):
    result = ProductoService.deleteProducto(id)
    if result['success']:
        return Response(result, status=200)
    else:
        return Response(result, status=400)