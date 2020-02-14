from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', KatalogView.as_view()),
    path('add_car',TambahKatalogView.as_view(),name='add_car'),
    path('save_car',SaveKatalog.as_view(),name='save_car'),
    path('delete/<int:id>',DeleteKatalog.as_view(),name='delete'),
    path('change/<int:id>',UpdateKatalog.as_view(),name='change'),
    path('ubah',UbahKatalog.as_view(),name='ubah'),
    
    
    # path('customers',KatalogCostumers.as_view(),name='ubah'),
]