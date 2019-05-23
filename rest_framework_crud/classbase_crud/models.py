from django.db import models

# Create your models here.
class ClassCrudModel(models.Model):
    name=models.CharField(max_length=30,null=False,blank=False)
    gender=models.CharField(max_length=10,null=False,blank=False)
    status=models.CharField(default='Inactive',max_length=20)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)