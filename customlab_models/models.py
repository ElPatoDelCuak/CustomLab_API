# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Caracteristicas(models.Model):
    id_caracteristica = models.AutoField(primary_key=True)
    caracteristica = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'caracteristicas'


class CaracteristicasProductos(models.Model):
    id_caracteristica = models.ForeignKey(Caracteristicas, models.DO_NOTHING, db_column='id_caracteristica')
    id_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='id_producto')

    class Meta:
        managed = False
        db_table = 'caracteristicas_productos'


class Carrito(models.Model):
    pk = models.CompositePrimaryKey('id_usuario', 'id_producto')
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario')
    id_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='id_producto')
    cantidad = models.IntegerField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'carrito'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ImagenesProductos(models.Model):
    id_imagen_producto = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='id_producto')
    ruta = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'imagenes_productos'


class ImagenesUsuario(models.Model):
    id_imagen_usuario = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario')
    ruta = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'imagenes_usuario'


class Incidencias(models.Model):
    id_incidencia = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario')
    tipo = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    estado = models.CharField(max_length=50)
    descripcion = models.TextField()

    class Meta:
        managed = False
        db_table = 'incidencias'


class Pedidos(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    id_usuario = models.IntegerField()
    estado = models.CharField(max_length=50)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(blank=True, null=True)
    direccion = models.CharField(max_length=255)
    numero_piso = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedidos'


class Productos(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=150)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    precio_costo = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    categoria = models.CharField(max_length=100)
    personalizable = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos'


class ProductosPedidos(models.Model):
    id_producto_pedido = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Productos, models.DO_NOTHING, db_column='id_producto')
    id_pedido = models.ForeignKey(Pedidos, models.DO_NOTHING, db_column='id_pedido')
    id_talla = models.ForeignKey('Tallas', models.DO_NOTHING, db_column='id_talla')
    cantidad = models.IntegerField()
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    beneficio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos_pedidos'


class ProductosPersonalizados(models.Model):
    id_producto_personalizado = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Productos, models.DO_NOTHING, db_column='id_producto')
    id_talla = models.ForeignKey('Tallas', models.DO_NOTHING, db_column='id_talla')
    id_imagen_usuario = models.ForeignKey(ImagenesUsuario, models.DO_NOTHING, db_column='id_imagen_usuario', blank=True, null=True)
    color = models.CharField(max_length=10)
    texto = models.CharField(max_length=255, blank=True, null=True)
    ruta_imagen_producto = models.TextField(blank=True, null=True)  # This field type is a guess.
    posicion_xy_texto = models.TextField(blank=True, null=True)  # This field type is a guess.
    posicion_xy_imagen = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'productos_personalizados'


class Tallas(models.Model):
    id_talla = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Productos, models.DO_NOTHING, db_column='id_producto')
    talla = models.CharField(max_length=10)
    stock = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tallas'


class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150)
    password = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=150)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    number_2fa = models.BooleanField(db_column='2fa', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    rol = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'
