from django.urls import path
from .views import productos_list

urlpatterns = [
    path('productos/', productos_list),
]
