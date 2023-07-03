from django.urls import path
from .views import home, poblar_bd, juego, juego_tienda, juego_ficha

urlpatterns = [
    path('', home, name="home"),
    path('poblar_bd', poblar_bd, name="poblar_bd"),
    path('juego/<action>/<id>', juego, name="juego"),
    path('juego_tienda', juego_tienda, name="juego_tienda"),
    path('juego_ficha/<id>', juego_ficha, name="juego_ficha"),
]
