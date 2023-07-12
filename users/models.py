from django.db import models

# Create your models here.
class User(models.Model):
	email = models.EmailField()
	name = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)
	state = models.BooleanField(default=True)

	def __str__(self):
		return f"{self.name} - {self.email}"
