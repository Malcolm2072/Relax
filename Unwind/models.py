from django.db import models

# Create your models here.

class MusicCategory(models.Model):
    c_id = models.IntegerField(primary_key=True)
    c_name = models.CharField(max_length=20)

    def __str__(self):
        return self.c_name
    
class Mood(models.Model):
    m_id = models.IntegerField(primary_key=True)
    m_name = models.CharField(max_length=20)

    def __str__(self):
        return self.m_name
      
class Music(models.Model):
    s_id = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    music = models.FileField(upload_to='Music')
    cover = models.FileField(upload_to='Music/Cover')
    m_id = models.ForeignKey(Mood, on_delete=models.CASCADE, null=True, blank=True)
    c_id = models.ForeignKey(MusicCategory,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.s_name