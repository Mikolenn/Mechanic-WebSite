from django.contrib import admin
from django.urls import path, include

from appointments import views
from register import views as viewsR

urlpatterns = [
    path('admin/', admin.site.urls),
    path('staff/', views.staff, name='staff'),
    path('staff/<int:pk>', views.staff, name='staff'),
    path('new/', views.new, name='new'),
    path('register/', viewsR.register, name='register'),
    path('', views.home, name='base'),
    path('', include("django.contrib.auth.urls")),
    path('view/', views.view, name='view'),
    path('view/<int:pk>', views.view, name='view'),
    path('create/', views.create, name='create'),
    path('create/<int:pk>', views.create, name='create'),
    path('delete/', views.delete, name='delete'),
    path('delete/<int:pk>', views.delete, name='delete'),

]
