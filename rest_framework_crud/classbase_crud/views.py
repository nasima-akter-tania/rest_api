from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ClassCrudSerializer
from .models import ClassCrudModel
from rest_framework import status
from django.http import Http404

# Create your views here.
class ClassCrudView(APIView):
    def get(self,request):
        all_data=ClassCrudModel.objects.all()
        serialized_data=ClassCrudSerializer(all_data,many=True)
        return Response(serialized_data.data)
    def post(self,request):
        serialized=ClassCrudSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data,status=status.HTTP_201_CREATED)
        return Response(serialized.errors,status=status.HTTP_400_BAD_REQUEST)
class ClassCrudDetails(APIView):
    def get_object(self,id):
        try:
            return ClassCrudModel.objects.get(id=id)
        except ClassCrudModel.DoesNotExist:
            raise Http404
    def get(self,request,id=None):
        instance_data=self.get_object(id)
        serialized=ClassCrudSerializer(instance_data)
        return Response(serialized.data)
    def put(self,request,id=None):
        instance=self.get_object(id)
        serialized_data=ClassCrudSerializer(instance,data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        return Response(serialized_data.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id=None):
        instance=self.get_object(id)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)