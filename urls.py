from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='userapp'),
    #path('detail/', views.forms, name='details'),
]
