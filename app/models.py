from django.db import models

class News(models.Model):
    public = models.CharField(max_length=250)
    date = models.DateField()
    
