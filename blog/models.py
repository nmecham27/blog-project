from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Post(models.Model):
	text = models.TextField()
	timeposted = models.DateTimeField(default=timezone.now)
	title = models.CharField(max_length=150)

	def __str__(self):
	    return self.title

