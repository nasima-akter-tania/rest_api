from rest_framework import serializers

from crud.models import CrudModel


class CrudSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrudModel
        fields = ('id','name','url','roll')
