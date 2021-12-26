from .views import index,add_point,get_points,get_my_locations,delete_point
from django.urls import path

urlpatterns = [
    path('',index),
    path('add_point',add_point),
    path('get_points',get_points),
    path('get_my_points',get_my_locations),
    path('delete_point/<int:id>',delete_point)
]