from django.db import models

class Game(models.Model):
    class Meta:
        db_table = 'game'
    
    username = models.CharField(max_length=50)
    score = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)