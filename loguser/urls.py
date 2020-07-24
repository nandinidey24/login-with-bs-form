from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.action),
    path('show/', views.display),
    path('signup/', views.data),
    path('', views.loguser)
]