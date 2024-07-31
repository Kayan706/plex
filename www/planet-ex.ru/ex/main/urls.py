from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('polit/', views.polit, name='polit'),
    path('pop/', views.pop, name='pop')
]