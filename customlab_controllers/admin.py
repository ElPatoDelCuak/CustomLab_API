from django.contrib import admin
from customlab_models.models import Productos, Usuarios, CaracteristicaProducto, Caracteristicas, Carrito, ImagenesProductos, ImagenesUsuario, Incidencias, Pedidos, ProductosPersonalizados, ProductosVendidos, Tallas

admin.site.register(Productos)
admin.site.register(Usuarios)
admin.site.register(Caracteristicas)
admin.site.register(Carrito)
admin.site.register(ImagenesProductos)
admin.site.register(ImagenesUsuario)
admin.site.register(Incidencias)
admin.site.register(Pedidos)
admin.site.register(ProductosPersonalizados)
admin.site.register(ProductosVendidos)
admin.site.register(Tallas)