from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = ('author', 'content', 'created_at', 'id', 'published_at', 'state',  'title', 'updated_at')
    read_only_fields = ('created_at', 'id')