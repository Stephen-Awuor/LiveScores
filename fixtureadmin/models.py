from django.db import models
from django.conf import settings
from teams.models import Teams
# Create your models here.
    
class Fixture(models.Model):
    STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('live', 'Live'),
        ('finished', 'Finished'),
    ]
    home_team = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name="home_fixtures")
    away_team = models.ForeignKey(Teams, on_delete=models.CASCADE, related_name="away_fixtures")
    match_date = models.DateTimeField()
    home_score = models.IntegerField(default=0)
    away_score = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='upcoming')

    def __str__(self):
        return f"{self.home_team} vs {self.away_team}"
