from django.contrib import admin
from django.urls import path,include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("register.urls")),
    path('', include("main.urls")),
    path('',include("django.contrib.auth.urls")),
]
