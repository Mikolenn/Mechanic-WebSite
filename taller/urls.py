from django.contrib import admin
from django.urls import path, include

from appointments import views
from register import views as viewsR

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show/', views.show, name='show'),
    path('show/<int:pk>', views.show, name='show'),
    path('new/', views.new, name='new'),
    path('register/', viewsR.register, name='register'),
    path('', views.base, name='base'),
    path('', include("django.contrib.auth.urls")),
]
