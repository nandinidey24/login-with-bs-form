from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.action),
    path('show/', views.display),
    path('', views.data),
]