from django.shortcuts import render
from django.http import  HttpResponseRedirect,HttpRequest
from .models import FunctionCrudModel
from .serializers import FunctionCrudSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def dataView(request):
    if request.method == 'GET':
        all_data=FunctionCrudModel.objects.all()
        serialized_data=FunctionCrudSerializer(all_data,many=True)
        return JsonResponse(serialized_data.data,safe=False)

    elif request.method == 'POST':
        json_parser=JSONParser()
        data=json_parser.parse(request)
        serialized=FunctionCrudSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return JsonResponse(serialized.data,status=201)
        return JsonResponse(serialized.errors,status=400)


