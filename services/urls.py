from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='services'),
    path('item/<int:item_id>', views.item_detail, name='item_detail'),
     path('service/signage/', views.service_view, {'service_id': 1}, name='signage'),
    path('service/display_signs/', views.service_view, {'service_id': 2}, name='display_signs'),
    path('service/digital_printing/', views.service_view, {'service_id': 3}, name='digital_printing'),
    path('service/vehicle_signs/', views.service_view, {'service_id': 4}, name='vehicle_signs'),


]