from rest_framework import viewsets, permissions, authentication
from .serializers import PostSerializer
from .models import Post

class PostViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.all()
	authentication_classes = [authentication.TokenAuthentication]
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = PostSerializer
