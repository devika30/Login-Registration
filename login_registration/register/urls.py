from django.urls import path

from . import views

appname='accounts'

urlpatterns = [
path("register/",views.register,name="register"),
path("logout/", views.logoutPage, name="logoutPage"),
path('login/',views.loginPage,name='loginPage'),
]