from django.db import models

# Create your models here.
class EnterTimentaly(models.Model):
    title=models.CharField(max_length=20, null=True, blank=True)
    image=models.ImageField(upload_to='intertaiment/images/', null=True, blank=True)
    audio=models.FileField(upload_to='intertaiment/audio/', null=True, blank=True)
    video =models.FileField(upload_to='intertaiment/video/', null=True, blank=True)
    description = models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title