from django.db import models


# Create your models here.
class CrudModel(models.Model):
    name = models.CharField(max_length=150)
    roll = models.IntegerField(unique=True)
    reg = models.IntegerField(unique=True)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TestModel(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    roll = models.IntegerField(unique=True, null=False, blank=False)
    status = models.CharField(default='Inactive', max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

