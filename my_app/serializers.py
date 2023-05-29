from rest_framework import serializers
from .models import *

class ProductUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
    

class InfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoModel
        fields = "__all__"
    

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersModel
        fields = "__all__"
    
    def validate(self, data):
        user_id = data.get('telegram_id')
        if UsersModel.objects.filter(telegram_id=user_id).exists():
            raise serializers.ValidationError("User with this id already exists")
        return data
    
class UserPUTLangSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersModel
        fields = ['lang']
 