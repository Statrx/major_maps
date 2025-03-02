
from django.urls import path
from . import views

urlpatterns = [
    path('map/', views.map_view, name='map_view'),
    path('potholes/',views.get_potholes,name='get_potholes'),
]
