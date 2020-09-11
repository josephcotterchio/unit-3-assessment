from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('task/<int:task_id>/', views.delete, name="delete"),
]
