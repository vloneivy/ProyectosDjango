from django.urls import path
from .views import home, poblar_bd, servicio, servicio_tienda, servicio_ficha

urlpatterns = [
    path('', home, name="home"),
    path('poblar_bd', poblar_bd, name="poblar_bd"),
    path('servicio/<action>/<id>', servicio, name="servicio"),
    path('servicio_tienda', servicio_tienda, name="servicio_tienda"),
    path('servicio_ficha/<id>', servicio_ficha, name="servicio_ficha"),
]
