from django.db import models
from django.contrib.auth.models import User

class Song(models.Model):
    user = models.ManyToManyField(User)
    songname = models.CharField(max_length=70)
    songduration = models.IntegerField()
    def written_by(self):
        return ",".join([str(p) for p in self.user.all()])

# Create your models here.
