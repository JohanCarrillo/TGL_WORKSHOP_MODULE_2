from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('email', 'name', 'created_at', 'id', 'state')
    read_only_fields = ('created_at', 'id')