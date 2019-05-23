from rest_framework import serializers
from .models import ClassCrudModel

class ClassCrudSerializer(serializers.ModelSerializer):
    class Meta:
        model=ClassCrudModel
        fields=('id','name','gender','status')