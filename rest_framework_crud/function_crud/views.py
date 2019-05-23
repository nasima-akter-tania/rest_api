from django.shortcuts import render
from django.http import  HttpResponseRedirect,HttpRequest
from .models import FunctionCrudModel
from .serializers import FunctionCrudSerializer
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
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
        data=json_parser.parse(request.data)
        serialized=FunctionCrudSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return JsonResponse(serialized.data,status=201)
        return JsonResponse(serialized.errors,status=400)

@csrf_exempt
def dataDetailsView(request,id):
    try:
        instance=get_object_or_404(FunctionCrudModel,id=id)
    except:
        return JsonResponse({'error':'Object Not found'},status=403)
    if request.method == 'GET':
        serializer=FunctionCrudSerializer(instance)
        return JsonResponse(serializer.data)
    elif request.method =='PUT':
        parser=JSONParser()
        data=parser.parse(request.data)
        update_serializer=FunctionCrudSerializer(instance,data=data)
        if update_serializer.is_valid():
            update_serializer.save()
            return JsonResponse(update_serializer.data,status=200)
        return JsonResponse(update_serializer.error,status=400)
    elif request.method == 'DELETE':
        instance.delete()
        return HttpRequest(status=204)


