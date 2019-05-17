from rest_framework import serializers
from .models import FunctionCrudModel
class FunctionCrudSerializer(serializers.ModelSerializer):
    class Meta:
        model=FunctionCrudModel
        fields=('id','name','gender','status')