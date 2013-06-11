import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

# each class is one object
# variables are attributes of the class
class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # To-string function
    def __unicode__(self):
        return self.question

    # customed function
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # To-string function
    def __unicode__(self):
        return self.choice_text
