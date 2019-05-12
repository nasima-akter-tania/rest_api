from django.urls import path,include
from . import views
from rest_framework import routers

crud_api_route=routers.DefaultRouter()
crud_api_route.register('crud',views.CrudView)

urlpatterns = [
  path('',include(crud_api_route.urls))
]