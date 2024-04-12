from django.db import models
from rest_framework import serializers
from .models import Member

class SerializerMember(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['memberId','username','password','firstname','lastname','email']