
from django.db import models

# Create your models here.
class Slider(models.Model):
    img = models.ImageField(upload_to="Slider")
    title = models.CharField(max_length=150)
    description = models.TextField()
    link = models.TextField()

    class Meta:
        verbose_name ='Slider'
        verbose_name_plural ='Sliders'
    
    def __str__(self):
        return self.title



    