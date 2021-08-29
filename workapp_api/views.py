from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework import generics, viewsets
from .serializers import ItemSerializer, UserSerializer
from .models import Item

class CreateUserView(generics.CreateAPIView):
  serializer_class = UserSerializer
  permission_classes = (AllowAny,)

class ItemListView(generics.ListAPIView):
  queryset = Item.objects.all()
  serializer_class = ItemSerializer
  permission_classes = (AllowAny,)

class ItemRetrieveView(generics.RetrieveAPIView):
  queryset = Item.objects.all()
  serializer_class = ItemSerializer
  permission_classes = (AllowAny,)

class ItemViewSet(viewsets.ModelViewSet):
  queryset = Item.objects.all()
  serializer_class = ItemSerializer
  # JWTが適用される