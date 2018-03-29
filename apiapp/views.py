from django.shortcuts import render

from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

from .permissions import IsOwner
from .serializers import BucketlistSerializer, UserSerializer
from .models import Bucketlist

from django.contrib.auth.models import User

class CreateView(generics.ListCreateAPIView):
    """This class handles the GET and POSt requests of our rest api."""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner)

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save(owner=self.request.user)



class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles GET, PUT, PATCH and DELETE requests."""

    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner)


class BucketView(generics.ListAPIView):
    """View to list the bucket queryset."""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer


class UserView(generics.ListAPIView):
    """View to list the user queryset."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """View to retrieve a user instance."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

# @api_view(['POST'])
# def create_user(request):
#     serialized = UserSerializer(data=request.data)
#     if serialized.is_valid():
#         serialized.save()
#         return Response(serialized.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['PUT'])
# def update_user(request, pk):
#     user = User.objects.get(pk=pk)

#     serialized = UserSerializer( user, data=request.data)
#     if serialized.is_valid():
#         serialized.save()
#         return Response(serialized.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['DELETE'])
# def delete_user(request, pk):
#     user = User.objects.get(pk=pk)
#     user.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)