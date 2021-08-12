from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import CustomUser
from account.serializers import RegisterSerializer


class RegisterView(APIView):
    def post(self, request):
        data = request.data
        print(data)
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Успешно зареган', 201)


class ActivationView(APIView):
    def get(self, request, email, activation_code):
        user = CustomUser.objects.filter(email=email, activation_code=activation_code).first()
        if not user:
            return Response('Такого юзера нету!', 400)
        user.activation_code = ''
        user.is_active = True
        user.save()
        return Response('Ваш аккаунт активен!', 200)

