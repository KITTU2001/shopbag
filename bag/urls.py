from django.contrib import admin
from django.urls import path
from bag.views import index,add_item,update_item,delete_item

urlpatterns = [
path('',index ,name='index'),
path('add-item',add_item,name="add-item"),
path('update-item/<int:item_id>', update_item, name='update-item'),
path('delete-item/<int:item_id>', delete_item, name='delete-item'),
]
