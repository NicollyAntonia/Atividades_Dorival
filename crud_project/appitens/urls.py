from django.urls import path
from . import views

urlpatterns = [
    path('',views.item_read,name='item_read'),
    path('n/', views.item_create, name='item_creat'),
    path('edit/<int:pk>', views.item_update, name='item_update'),
    path('delete/<int:pk>', views.item_delete, name='item_delete'),
]