from rest_framework import serializers

from crud.models import CrudModel,TestModel


class CrudSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrudModel
        fields = ('id','name','url','roll')
class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model=TestModel
        fields=('name','roll','status','created_at')