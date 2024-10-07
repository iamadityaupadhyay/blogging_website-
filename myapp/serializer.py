from .models import *
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =UserImage
        fields="__all__"