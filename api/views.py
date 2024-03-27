from django.shortcuts import render
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book
from .serializers import BookSerializer
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

User=get_user_model()


class Login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:            
            refresh = RefreshToken.for_user(user)
            return Response({"user":str(user),"message":"Login Success","refresh": str(refresh),"access": str(refresh.access_token),},
            status=status.HTTP_302_FOUND)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class Logout(APIView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': 'Logout success'}, status=status.HTTP_200_OK)
        except:
            return Response({'message': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
    
class Register(APIView):
    def post(self, request):
        try:
            if request.data.get('username') is None or request.data.get('password') is None:
                return Response({'message': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)
            username = request.data.get('username')
            password = request.data.get('password')
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'message': f'{e}'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'message': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)
    

class BookList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BookDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get_object(self, isbn):
        try:
            return Book.objects.get(isbn=isbn)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, isbn):
        book = self.get_object(isbn)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, isbn):
        book = self.get_object(isbn)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, isbn):
        book = self.get_object(isbn)
        book.delete()
        return Response({'message':'Book deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
