from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cars/', views.show_all_cars, name='allcars'),
    path('cars/<int:car_id>', views.get_one_car, name='car'),
]
