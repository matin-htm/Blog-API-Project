from django.contrib.auth import get_user_model
from rest_framework import generics

from .serializers import UserListSerializer, UserDetailSerializer


class UserListView(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserListSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserDetailSerializer
