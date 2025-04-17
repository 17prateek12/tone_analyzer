from django.db import models

# Create your models here.
class ActionAnalyzer(models.Model):
    query = models.TextField()
    tone = models.CharField(max_length=100)
    intent = models.CharField(max_length=100)
    suggested_action = models.JSONField()
    
    def __str__(self):
        return f"{self.query}"
