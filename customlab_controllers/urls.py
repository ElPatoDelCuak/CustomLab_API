from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView


from .controllers.productoController import getFeaturedProducts, getProductos, getProductoById, createProducto, updateProducto, deleteProducto
from .controllers.usuarioController import getUsuarios, getUsuarioById, createUsuario, updateUsuario, deleteUsuario, loginUsuario
from .controllers.incidenciaController import getIncidencias, getIncidenciaById, createIncidencia, updateEstadoIncidencia, deleteIncidencia
from .controllers.productoPersonalizadoController import getProductosPersonalizados, getProductoPersonalizadoById, createProductoPersonalizado, updateProductoPersonalizado, deleteProductoPersonalizado
from .controllers.pedidoController import getPedidos, getPedidoById, createPedido, updatePedido, deletePedido
from .controllers.userImagesController import getImagesByUserId, uploadImage, deleteImage
from .controllers.productImagesController import getProductImagesByProductId, deleteProductImage, uploadProductImage
from .controllers.tallaController import getTallas, getTallasByProductoId, createTalla, updateTalla, deleteTalla
from customlab_controllers.controllers.caracteristicaController import addCaracteristicaToProducto, createCaracteristica, deleteCaracteristica, getCaracteristicas, removeCaracteristicaFromProducto


urlpatterns = [
    #Productos URLs
    path('productos/', getProductos),
    path('productos/<int:id>/', getProductoById),
    path('productos/featured/', getFeaturedProducts),
    path('productos/create/', createProducto),
    path('productos/update/<int:id>/', updateProducto),
    path('productos/delete/<int:id>/', deleteProducto),
    #Usuario URLs
    path('usuarios/', getUsuarios),
    path('usuario/<int:id>/', getUsuarioById),
    path('usuarios/create/', createUsuario),
    path('login/', loginUsuario),
    path('login/refresh/', TokenRefreshView.as_view()),
    path('login/verify/', TokenVerifyView.as_view()),
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
    #Productos Personalizados URLs
    path('producto_personalizado/', getProductosPersonalizados),
    path('producto_personalizado/<int:id>/', getProductoPersonalizadoById),
    path('producto_personalizado/create/', createProductoPersonalizado),
    path('producto_personalizado/update/<int:id>/', updateProductoPersonalizado),
    path('producto_personalizado/delete/<int:id>/', deleteProductoPersonalizado),
    # Images URLs
    path('images/user/<int:user_id>/', getImagesByUserId),
    path('images/upload/', uploadImage),
    path('images/delete/<int:image_id>/', deleteImage),
    # Product Images URLs
    path('images/product/<int:product_id>/', getProductImagesByProductId),
    path('images/product/<int:product_id>/create/', uploadProductImage),
    path('images/product/<int:product_id>/delete/', deleteProductImage),
    # Tallas URLs
    path('tallas/', getTallas),
    path('tallas/producto/<int:producto_id>/', getTallasByProductoId),
    path('tallas/create/', createTalla),
    path('tallas/update/<int:id>/', updateTalla),
    path('tallas/delete/<int:id>/', deleteTalla),
    # Caracteristicas URLs
    path('caracteristicas/', getCaracteristicas),
    path('caracteristicas/create/', createCaracteristica),
    path('caracteristicas/delete/<int:id>/', deleteCaracteristica),
    path('caracteristicas/add_to_producto/', addCaracteristicaToProducto),
    path('caracteristicas/remove_from_producto/', removeCaracteristicaFromProducto),
]