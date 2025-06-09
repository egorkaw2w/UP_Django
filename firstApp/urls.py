from django.contrib import admin
from django.urls import path
from .views import firstPage,About, Catalog, ItemPage

urlpatterns = [
    path('', firstPage),
    path('About', About),
    path('catalog',Catalog),

    path('ItemPage', ItemPage)
]
