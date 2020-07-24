from django.urls import path
from . import views

urlpatterns = [
    path('form', views.action, name="form"),
    path('show', views.display, name="show"),
    path('signup', views.data, name="signup"),
    path('', views.loguser, name="")
]