from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Page(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=128)
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title