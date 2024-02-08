from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import CustomUser
from .serializers import UserSerializer, FullUserSerializer


class CustomUserList(APIView):
    def get_serializer_class(self):
        if self.request.user.is_staff:
            return FullUserSerializer
        return UserSerializer

    def get(self, request):
        users = CustomUser.objects.all()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(users, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = FullUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CustomUserDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return FullUserSerializer
        return UserSerializer
        
    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(user)
        return Response(serializer.data)
    
    def delete(self, request, pk):
        user = self.get_object(pk)

        if user != request.user and not request.user.is_staff:
            return Response({'message': 'You do not have permission to delete this user account'},status=status.HTTP_403_FORBIDDEN)
        
        user.delete()
        return Response({'message': 'User deleted.'}, status=status.HTTP_202_ACCEPTED)    