from django.db import models

# Create your models here.
class Post(models.Model):
	author = models.CharField(max_length=200)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	published_at = models.DateField()
	state = models.BooleanField(default=True)
	title = models.CharField(max_length=200)
	updated_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.title} - {self.author}"