from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone    
# Create your models here.
class Todo(models.Model):
    content = models.TextField()
    time=models.TimeField(default=timezone.now(),null=True)
    date = models.DateField(default=datetime.now(),null=True)
    user = models.ForeignKey(User, on_delete= models.CASCADE, null = True, blank = True)
    mark = models.BooleanField(default=False)

    def __str__(self):
        return self.content
