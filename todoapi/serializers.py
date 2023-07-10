from rest_framework import serializers
from django.contrib.auth.models import User
from tasks.models import Todo



class UserSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=User
        fields=["id","username","email","password"]


    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

# create(),update()

class TodoSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    date=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)   
    class Meta:
        model=Todo
        fields="__all__"