from django.urls import path

from .import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('register', views.register, name="register"),
    path('successful', views.success, name="suceess"),
    path('login', views.login, name='login')

]