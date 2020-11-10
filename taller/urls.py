from django.contrib import admin
from django.urls import path, include

from appointments import views
from register import views as viewsR

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show/', views.show, name='show'),
    path('show/<int:pk>', views.show, name='show'),
    path('staff/', views.show, name='staff'),
    path('new/', views.new, name='new'),
    path('register/', viewsR.register, name='register'),
    path('', views.home, name='base'),
    path('', include("django.contrib.auth.urls")),
    path('view/', views.view, name='view'),
    path('view/<int:pk>', views.view, name='view'),
    path('create/', views.create, name='create'),
]
