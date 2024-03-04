from django.urls import path
from . import views

urlpatterns = [
    path('estifo/', views.hello_world, name='hello_world'),
]