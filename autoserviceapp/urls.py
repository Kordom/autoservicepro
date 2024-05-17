from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cars/', views.show_all_cars, name='allcars'),
    path('cars/<int:car_id>', views.get_one_car, name='car'),
    path('orders/', views.UzsakymasListView.as_view(), name='allorders'),
    path('orders/<int:pk>', views.UzsakymasDetailedView.as_view(), name='order'),
    path('curorders/', views.get_all_current_orders_count, name='curorders'),
    path('search/', views.search, name='search'),

]
