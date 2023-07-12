from django.urls import include, path
from rest_framework import routers
from .views import PostViewSet, get_user_post, celery_sum, task_no_celery, task_celery

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = router.urls
urlpatterns.append(path("/get_user_post", get_user_post))
urlpatterns.append(path("/celery-sum", celery_sum))
urlpatterns.append(path("/celery-task", task_no_celery))
urlpatterns.append(path("no-celery-task", task_celery))