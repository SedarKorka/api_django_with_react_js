from django.shortcuts import render
from . import models
import requests
from django.http import JsonResponse
from . import serializers
from rest_framework.views import APIView
from users.models import Member
from .serializers import SerializerMember

# Create your views here.
class MemberView(APIView):
    def get_member(self, memberId):
        try:
            member = Member.objects.get(memberId=memberId)
            return member
        except Exception as e:
            print("The error is: ",e)
    def get(self , request, memberId=None):
        if memberId:
            data = self.get_member(memberId)
            serialize = SerializerMember(data)
        else:
            data = Member.objects.all()
            serialize = SerializerMember(data,many=True)
        return JsonResponse(serialize.data)

    def post(self, request):
        data = request.data
        serialize = SerializerMember(data=data)
        if serialize.is_valid():
            serialize.save()
            return JsonResponse("New member added successfully.",safe=False)
        return JsonResponse("Fail to add a new member.", safe=False)

    def put(self , request, memberId=None):
        member = Member.objects.get(memberId=memberId)
        serialize = SerializerMember(instance= member, data = request.data, partial=True)
        if serialize.is_valid():
            serialize.save()
            return JsonResponse("User update successfully.", safe=False)
        return JsonResponse("Couldn't update member.", safe=False)
    
    def delete(self, request, memberId):
        member = Member.objects.get(memberId=memberId)
        member.delete()
        return JsonResponse("Member delete successfully", safe=False)