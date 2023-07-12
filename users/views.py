from rest_framework import viewsets, permissions, authentication
from .serializers import UserSerializer
from .models import User

class UserViewSet(viewsets.ModelViewSet):
	"""
		retrieve:
		Return the given user.

		list:
		Return a list of all existing users.

		create:
		Create a new user instance.
		"""
	queryset = User.objects.all()
	authentication_classes = [authentication.TokenAuthentication]
	permission_classes = [permissions.IsAdminUser]
	serializer_class = UserSerializer