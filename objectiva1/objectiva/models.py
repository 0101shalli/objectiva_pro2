import time

from django.db import models
from django.contrib.auth.models import User
import datetime
from datetime import datetime
# Create your models here.
class activity(models.Model):
    user = models.ForeignKey(User, max_length=100, on_delete=models.CASCADE, related_name='Activity', null=True,
                             blank=True)
    activityName = models.CharField(max_length=100)
    description = models.TextField(max_length=100000, default='These activity will surely be a success')
    startingTime = models.DateTimeField()
    endingTime = models.DateTimeField()
    complete = models.BooleanField( default=False)
    notificationMode = models.IntegerField(default=5)
    create_time= models.DateTimeField( default=datetime.now)

    def _str_(self):
        return self.notificationMode
    class meta:
        odering=['complete']


class activity_name(models.Model):
    Activity = models.ForeignKey(activity,default='none ' ,on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)
    def _str_(self):
        return self.activity

