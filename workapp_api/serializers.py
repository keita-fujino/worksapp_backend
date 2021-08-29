from django.db.models import fields
from rest_framework import serializers
from .models import Item
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'password')
    extra_kwargs = {
      'password': {
        'write_only': True,
        'required': True
      }
    }
  
  def create(self, validated_data):
    user = User.objects.crate_user(**validated_data)
    return user

class ItemSerializer(serializers.ModelSerializer):
  created_at = serializers.DateTimeField(
    format = "%Y-%m-%d %H:%M:%S",
    read_only = True,
  )
  class Meta:
    model = Item
    fields = ('id', 'firstName', 'middleName', 'lastName', 'age', 'sex', 'memo', 'created_at', 'created_by')
