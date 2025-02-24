from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='services'),
    path('item/<int:item_id>', views.item_detail, name='item_detail'),

]