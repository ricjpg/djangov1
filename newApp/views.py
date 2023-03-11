from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django_framework.parser import JSONParser
from django.http import HttpResponse

from newApp.models import Users
from newApp.serializers import UserSerializer

# Create your views here.


@csrf_exempt
def userApi(request):
    if request.method == 'GET':
        users = Users.objects.all()
        user_serializer = UserSerializer(users, many=True)
        return JsonResponse(user_serializer.data,safe=True)
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data, many=True)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added user",safe=True)
        return JsonResponse("Failed to add",safe=True)
    # elif request.method=='PUT':
