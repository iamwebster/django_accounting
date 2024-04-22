from django.urls import path 
from . import views 


urlpatterns = [
    path('stocks/', views.StockView.as_view()),
    path('stocks/<int:pk>/', views.StockDetailView.as_view()),
    path('categories/', views.CategoryView.as_view()),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view()),
    path('equipments/', views.EquipmentView.as_view()),
    path('equipments/<int:pk>/', views.EquipmentDetailView.as_view()),
]
