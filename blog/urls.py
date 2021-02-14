from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('all',views.photo_list, name='photo_list' ),
]