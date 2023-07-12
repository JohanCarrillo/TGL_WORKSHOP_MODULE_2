from rest_framework import viewsets, permissions, authentication, response
from django.core.cache import cache
from django.http import HttpResponse
from .serializers import PostSerializer
from .models import Post
from .tasks import add, long_task

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

def celery_sum(request):
    # La tarea se ejecutará en segundo plano y la vista retornará inmediatamente.
    result = add.delay(4, 4)
    print(result.get(timeout=10))
    return HttpResponse('Task has been run')

def task_no_celery(request):
    long_task()
    return HttpResponse('Task without celery')

def task_celery(request):
    long_task.delay()
    return HttpResponse('Task with celery')