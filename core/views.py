from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Productos

@api_view(['GET'])
def productos_list(request):
    """Return all records from the `productos` table."""
    qs = Productos.objects.all().values(
        'id_producto', 'nombre_producto', 'precio_venta', 'precio_costo',
        'stock', 'categoria', 'personalizable'
    )
    return Response(list(qs))

