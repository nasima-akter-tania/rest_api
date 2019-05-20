from django.urls import path
from .views import dataView,dataDetailsView
urlpatterns=[
    path('all_data',dataView),
    path('all_data/<int:id>',dataDetailsView)
]
