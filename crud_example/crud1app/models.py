from django.db import models

# Create your models here.
class RunCodes(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    
    def __str__(self):
        return self.title