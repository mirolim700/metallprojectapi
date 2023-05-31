from rest_framework import serializers
from .models import *

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductsModel
        fields = "__all__"

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoModel
        fields = "__all__"

class CustomUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersModel
        fields = ["id", "username", "telegram_id"]

    def validate(self, data):
        user_id = data.get('telegram_id')
        if UsersModel.objects.filter(telegram_id=user_id).exists():
            raise serializers.ValidationError('User with this id already exists!')
        return data
    
class UserPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersModel
        fields = ["lang"]