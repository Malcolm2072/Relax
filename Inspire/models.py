from django.db import models

# Create your models here.

class Story(models.Model):
    p_id = models.IntegerField(primary_key=True)
    p_name = models.CharField(max_length=100)
    stories = models.TextField()
    pic = models.FileField(upload_to='img')

    def __str__(self):
        return self.p_name