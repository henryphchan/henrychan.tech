from django.urls import path
from . import views

urlpatterns = [
    path('', views.supplier_list, name='supplier_list'),
    path('new/', views.supplier_create, name='supplier_create'),
    path('edit/<int:pk>/', views.supplier_update, name='supplier_update'),
    path('delete/<int:pk>/', views.supplier_delete, name='supplier_delete'),
]