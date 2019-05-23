from django.urls import path
from .views import *
urlpatterns=[
    path('',ClassCrudView.as_view()),
    path('<int:id>/',ClassCrudDetails.as_view())
]