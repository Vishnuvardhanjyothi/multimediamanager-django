from django.db import models

class youtube(models.Model):
    desc=models.TextField()
    image=models.ImageField(upload_to='image/')
    video=models.FileField(upload_to='video/')
    audio=models.FileField(upload_to='audio/')
