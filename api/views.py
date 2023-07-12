from rest_framework import viewsets, permissions, authentication
from .serializers import PostSerializer
from .models import Post

class PostViewSet(viewsets.ModelViewSet):
	"""
		retrieve:
		Return the given post.

		list:
		Return a list of all existing posts.

		create:
		Create a new post instance.
		"""
	queryset = Post.objects.all()
	authentication_classes = [authentication.TokenAuthentication]
	permission_classes = [permissions.IsAuthenticated]
	serializer_class = PostSerializer
