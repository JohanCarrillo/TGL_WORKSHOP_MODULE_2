from rest_framework import viewsets, permissions, authentication, response
from django.core.cache import cache
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

def caching(some_func):
    def wraper(*args, **kwargs):
        user_posts_cache = cache.get("user_posts")
        if not user_posts_cache:
            user_posts = some_func(*args, **kwargs)
        cache.set("user_posts", user_posts, 600)
        return user_posts
    return wraper

# get author of post
@caching
def get_user_post(request):
  post_id = request.GET.get('post_id')
  try:
    post = Post.objects.get(id = post_id)
    author = post.author
    return response.Response({'author': author.username})
  except Post.DoesNotExist:
        return response.Response({'error': 'Post not found'}, status=404)