from django.urls import path
from .views import  dataView
urlpatterns=[
    path('all_data',dataView)
]
