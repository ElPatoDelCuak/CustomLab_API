from django.urls import path
from .controllers.productoController import getProductos, getProductoById, createProducto, updateProducto, deleteProducto
from .controllers.usuarioController import getUsuarios, getUsuarioById, createUsuario, updateUsuario, deleteUsuario
from .controllers.pedidoController import getPedidos, getPedidoById, createPedido, updatePedido, deletePedido
from .controllers.incidenciaController import getIncidencias, getIncidenciaById, createIncidencia, updateEstadoIncidencia, deleteIncidencia
from .controllers.userImagesController import getImagesByUserId, uploadImage, deleteImage

urlpatterns = [
    #Productos URLs
    path('productos/', getProductos),
    path('productos/<int:id>/', getProductoById),
    path('productos/create/', createProducto),
    path('productos/update/<int:id>/', updateProducto),
    path('productos/delete/<int:id>/', deleteProducto),
    #Usuario URLs
    path('usuarios/', getUsuarios),
    path('usuario/<int:id>/', getUsuarioById),
    path('usuarios/create/', createUsuario),
    path('usuarios/update/<int:id>/', updateUsuario),
    path('usuarios/delete/<int:id>/', deleteUsuario),
    # Pedido URLs
    path('pedidos/', getPedidos),
    path('pedido/<int:id>/', getPedidoById),
    path('pedidos/create/', createPedido),
    path('pedidos/update/<int:id>/', updatePedido),
    path('pedidos/delete/<int:id>/', deletePedido),
    #Incidencias URLs
    path('incidencias/', getIncidencias),
    path('incidencias/<int:id>/', getIncidenciaById),
    path('incidencias/create/', createIncidencia),
    path('incidencias/update/<int:id>/', updateEstadoIncidencia),
    path('incidencias/delete/<int:id>/', deleteIncidencia),
    # Images URLs
    path('images/user/<int:user_id>/', getImagesByUserId),
    path('images/upload/', uploadImage),
    path('images/delete/<int:image_id>/', deleteImage),
]