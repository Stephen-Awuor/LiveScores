from django.db import models
from django.conf import settings
# Create your models here.
    
class Teams(models.Model):
    team_name = models.CharField(max_length=200, blank=True)
    age_group = models.CharField(max_length=200, blank=True)
    gender = models.CharField(max_length=15, blank=True)
    sport = models.CharField(max_length=15, blank=True)
    coach = models.CharField(max_length=15, blank=True)
    email = models.EmailField(unique=False)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.team_name
