from django.urls import include, path
from rest_framework import routers
from .views import PostViewSet, get_user_post

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = router.urls
urlpatterns.append(path("/get_user_post", get_user_post))