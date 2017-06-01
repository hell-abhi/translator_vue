from rest_framework import serializers
from .models import User

from rest_framework.response import Response
from rest_framework import status

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('user_id','first_name','last_name','email_id')