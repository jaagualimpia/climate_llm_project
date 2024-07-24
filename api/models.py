from django.db import models

# Create your models here.
class QueryBasicModel(models.Model):
    query = models.CharField(max_length=2500)
    query_at = models.DateTimeField(auto_now_add=True)
    response = models.CharField(max_length=3000, blank=True) 