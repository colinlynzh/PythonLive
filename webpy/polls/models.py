from django.db import models
from django.utils import timezone

# Create your models here.
class  Poll(models.Model):

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <  now
	

