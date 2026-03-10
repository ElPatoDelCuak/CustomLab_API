from django.contrib import admin
from django.utils.html import format_html
from django.contrib import messages
from customlab_models.models import (
    Productos, Usuarios, CaracteristicaProducto, Caracteristicas,
    Carrito, ImagenesProductos, ImagenesUsuario, Incidencias,
    Pedidos, ProductosPersonalizados, ProductosVendidos, Tallas
)


# ─── INLINES ────────────────────────────────────────────────────────────────

class TallasInline(admin.TabularInline):
    model = Tallas
    extra = 3
    fields = ('talla', 'stock')


class ImagenesProductosInline(admin.TabularInline):
    model = ImagenesProductos
    extra = 2
    fields = ('ruta', 'preview')
    readonly_fields = ('preview',)

    def preview(self, obj):
        if obj.ruta:
            return format_html('<img src="{}" style="height:60px; border-radius:4px"/>', obj.ruta)
        return "-"
    preview.short_description = "Vista previa"


class CaracteristicaProductoInline(admin.TabularInline):
    model = CaracteristicaProducto
    extra = 2
    fields = ('id_caracteristica',)
    verbose_name = "Característica"
    verbose_name_plural = "Características del producto"


# ─── PRODUCTOS ───────────────────────────────────────────────────────────────

@admin.register(Productos)
class ProductosAdmin(admin.ModelAdmin):
    inlines = [ImagenesProductosInline, TallasInline, CaracteristicaProductoInline]

    list_display = ('id_producto', 'nombre_producto', 'categoria', 'precio_venta', 'precio_costo', 'stock', 'personalizable')
    list_filter = ('categoria', 'personalizable')
    search_fields = ('nombre_producto', 'categoria')
    list_editable = ('stock', 'precio_venta')

    fieldsets = (
        ('Información básica', {
            'fields': ('nombre_producto', 'categoria', 'personalizable')
        }),
        ('Precios y stock', {
            'fields': ('precio_venta', 'precio_costo', 'stock')
        }),
    )

    def save_model(self, request, obj, form, change):
        """
        Al guardar desde el admin, usamos directamente el ORM.
        Las imágenes se gestionan desde el inline de ImagenesProductos.
        Si necesitas lógica especial de tu ProductoService, llámala aquí.
        """
        super().save_model(request, obj, form, change)
        action = "actualizado" if change else "creado"
        self.message_user(request, f'Producto "{obj.nombre_producto}" {action} correctamente.', messages.SUCCESS)

    def delete_model(self, request, obj):
        """
        Al eliminar, reutilizamos la lógica de ProductoService
        para que también borre las imágenes del disco.
        """
        from customlab_services.services.productoService import ProductoService
        result = ProductoService.deleteProducto(obj.id_producto)
        if result['success']:
            self.message_user(request, f'Producto "{obj.nombre_producto}" eliminado junto con sus imágenes.', messages.SUCCESS)
        else:
            self.message_user(request, result['message'], messages.ERROR)


# ─── USUARIOS ────────────────────────────────────────────────────────────────

@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'nombre', 'apellidos', 'email', 'rol', 'doble_factor')
    list_filter = ('rol', 'doble_factor')
    search_fields = ('nombre', 'apellidos', 'email')
    readonly_fields = ('password',)  # no editar contraseña desde aquí

    fieldsets = (
        ('Datos personales', {
            'fields': ('nombre', 'apellidos', 'email', 'fecha_nacimiento')
        }),
        ('Cuenta', {
            'fields': ('rol', 'doble_factor', 'password')
        }),
    )


# ─── PEDIDOS ─────────────────────────────────────────────────────────────────

@admin.register(Pedidos)
class PedidosAdmin(admin.ModelAdmin):
    list_display = ('id_pedido', 'id_usuario', 'estado', 'total', 'fecha')
    list_filter = ('estado',)
    search_fields = ('id_usuario__nombre', 'id_usuario__email')
    readonly_fields = ('fecha',)

    # Acción para marcar pedidos como enviados
    actions = ['marcar_enviado', 'marcar_entregado']

    def marcar_enviado(self, request, queryset):
        updated = queryset.update(estado='enviado')
        self.message_user(request, f'{updated} pedido(s) marcados como enviados.')
    marcar_enviado.short_description = "Marcar seleccionados como → Enviado"

    def marcar_entregado(self, request, queryset):
        updated = queryset.update(estado='entregado')
        self.message_user(request, f'{updated} pedido(s) marcados como entregados.')
    marcar_entregado.short_description = "Marcar seleccionados como → Entregado"


# ─── INCIDENCIAS ─────────────────────────────────────────────────────────────

@admin.register(Incidencias)
class IncidenciasAdmin(admin.ModelAdmin):
    list_display = ('id_incidencia', 'id_usuario', 'tipo', 'estado_incidencia', 'fecha')
    list_filter = ('tipo', 'estado_incidencia')
    search_fields = ('id_usuario__nombre', 'descripcion')
    readonly_fields = ('fecha',)

    actions = ['marcar_resuelta']

    def marcar_resuelta(self, request, queryset):
        updated = queryset.update(estado_incidencia='resuelta')
        self.message_user(request, f'{updated} incidencia(s) marcadas como resueltas.')
    marcar_resuelta.short_description = "Marcar seleccionadas como → Resuelta"


# ─── RESTO DE MODELOS ─────────────────────────────────────────────────────────

@admin.register(Caracteristicas)
class CaracteristicasAdmin(admin.ModelAdmin):
    list_display = ('id_caracteristica', 'caracteristica')
    search_fields = ('caracteristica',)


@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    list_display = ('id_usuario', 'id_producto', 'cantidad', 'precio_total')
    search_fields = ('id_usuario__nombre',)


@admin.register(ImagenesProductos)
class ImagenesProductosAdmin(admin.ModelAdmin):
    list_display = ('id_imagen_producto', 'id_producto', 'preview')
    readonly_fields = ('preview',)

    def preview(self, obj):
        if obj.ruta:
            return format_html('<img src="{}" style="height:80px; border-radius:4px"/>', obj.ruta)
        return "-"
    preview.short_description = "Vista previa"


@admin.register(ImagenesUsuario)
class ImagenesUsuarioAdmin(admin.ModelAdmin):
    list_display = ('id_imagen_usuario', 'id_usuario', 'ruta')


@admin.register(ProductosVendidos)
class ProductosVendidosAdmin(admin.ModelAdmin):
    list_display = ('id_producto_vendido', 'id_producto', 'id_pedido', 'id_talla', 'cantidad', 'precio_venta', 'beneficio')
    readonly_fields = ('beneficio',)


@admin.register(ProductosPersonalizados)
class ProductosPersonalizadosAdmin(admin.ModelAdmin):
    list_display = ('id_producto_personalizado', 'id_producto', 'id_talla', 'color', 'texto')