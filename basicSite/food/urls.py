from .views import *
from django.urls import path

app_name = 'food'
urlpatterns = [
    path('', IndexClassView.as_view(), name='index'),
    path('<int:pk>/', FoodDetail.as_view(), name='detail'),
    path('item/', item, name='item'),
    # add items
    path('add/', CreateItem.as_view(), name='createItem'),
    # update item 
    path('update/<int:id>', updateItem, name='updateItem'),
    # delete item
    path('delete/<int:id>', deleteItem, name='deleteItem'),
]
