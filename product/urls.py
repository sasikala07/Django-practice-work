from .views import display
from .views import dispalyprodlist
from .views import addtocart , displaycart

from django.urls import path

urlpatterns = [
    path('details/<int:pid>', display),

    path('list', dispalyprodlist),
    path('addtocart',addtocart),
    path('cart',displaycart),
]
