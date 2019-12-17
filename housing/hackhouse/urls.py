from django.urls import path

from .import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('register', views.register, name="register"),
    path('successful', views.success, name="suceess"),
    path('login', views.user_login, name='login'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about')

]