from django.db import models

class Game(models.Model):
    username = models.CharField(max_length=50)
    score = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    
    ghost_data = models.JSONField(null=True, blank=True)
    duration = models.FloatField(null=True, blank=True)
    
    class Meta:
        db_table = 'game'