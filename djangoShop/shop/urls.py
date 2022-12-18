from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<slug:slug>/', views.show, name='show'),
    path('delete/<slug:slug>', views.delete, name="delete"),
    path('edit/<slug:slug>', views.edit, name="edit"),
]