from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import CustomUser
from .serializers import CustomUserSerializer
from .permissions import IsUserOrReadOnlyUser


class CustomUserList(APIView):
    
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CustomUserDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnlyUser]

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, pk):
        user = self.get_object(pk)
        
        if user != request.user:
            return Response(
                {"message": "You do not have permission to perform this action"},
                status=status.HTTP_403_FORBIDDEN
            )
        
        serializer = CustomUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        user = self.get_object(pk)

        if not request.user.is_staff:
            return Response(
                {"message": "You do not have permission to perform this action"},
                status=status.HTTP_403_FORBIDDEN
            )

        user.delete()
        return Response({"message: User successfully deleted"}, status=status.HTTP_200_OK)
    