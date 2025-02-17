from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_order, name='add_order'),
    path('edit/<int:id>/', views.edit_order, name='edit_order'),
    path('delete/<int:id>/', views.delete_order, name='delete_order'),
    path('view/<int:id>/', views.view_order, name='view_order'),
]
