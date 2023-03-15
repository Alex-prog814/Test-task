from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from applications.user.serializers import RegisterSerializer, UserSerializer, TransactionSerializer

User = get_user_model()

class RegisterView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Successfully registration!', status=status.HTTP_201_CREATED)

class TransactionView(APIView):
    def post(self, request):
        data = request.data
        serializer = TransactionSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            return Response('Successfully transaction!', status=status.HTTP_200_OK)

class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
