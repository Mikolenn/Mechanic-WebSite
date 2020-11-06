from django.contrib import admin
from django.urls import path

from appointments import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show/', views.show, name='show'),
    path('show/<int:pk>', views.show, name='show'),
    path('new/', views.new, name='new'),
]
