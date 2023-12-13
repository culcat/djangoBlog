from django.contrib.auth.models import User
from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True,blank=True)
