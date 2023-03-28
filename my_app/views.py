from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response 
from rest_framework.views import APIView
from .serializers import *
from .models import *

class UserView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductUserSerializer(products, many=True)
        if serializer:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductByIdView(APIView):
    def get(self, request, pk):
        products = Product.objects.filter(pk =pk )
        print(products, '*'*5)
        serializer = ProductUserSerializer(products, many=True)
        if serializer:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InfoView(APIView):
    def get(self, request):
        info = InfoModel.objects.all()
        serializer = InfoModelSerializer(info, many=True )
        if serializer:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserPutLangSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersModel
        fields = ['lang']


