from django.urls import path
from . import views

urlpatterns = [
    path('myapp/', views.myapp, name='myapp'),
    path('product/', views.product, name='product'),
    path('aboutme/', views.aboutme, name='aboutme'),
]