
from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SignUpSerializer
from .tokens import create_jwt_pair_for_user

# Criar e logar usuário
class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    permission_classes = []

    def post(self, request: Request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {"message": "Usuário criado com sucesso", "data": serializer.data}

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request: Request, id):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {"message": "Usuário alterado com sucesso", "data": serializer.data}

            return Response(data=response, status=status.HTTP_)

"""
class EditView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SignUpSerializer
    
    def put(self, request, id=None):
        user = User.objects.filter(id=id)
        drinks = Drink.objects.filter(id=id)
        serializer = DrinkSerializer(drinks, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
"""

class LoginView(APIView):
    serializer_class = SignUpSerializer
    permission_classes = []

    def post(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email, password=password)

        if user is not None:
            tokens = create_jwt_pair_for_user(user)

            response = {"message": "Logado com sucesso", "access": tokens['access'], "refresh": tokens['refresh']}
            return Response(data=response, status=status.HTTP_200_OK)

        else:
            return Response(data={"message": "Email ou senha inválido", "error": "login error"})

    def get(self, request: Request):
        content = {"user": str(request.user), "auth": str(request.auth)}
        
        return Response(data=content, status=status.HTTP_200_OK)

