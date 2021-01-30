
from django.db import models

# Create your models here.
class abouts(models.Model):
    title = models.TextField()
    description = models.TextField()
    link = models.TextField()
    img = models.ImageField(upload_to="about")
    video = models.TextField()
    button = models.TextField()
    
    def __str__(self):
        return self.title







class flavor(models.Model):
    name = models.CharField(max_length=30)
    img = models.ImageField( upload_to="Flavor", blank="true", null="true")

    class Meta:
        verbose_name ='Flavor'
        verbose_name_plural ='Flavors'
    
    def __str__(self):
        return self.name

class chocolate(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to="Product")
    flavor = models.ManyToManyField("flavor", verbose_name=("flavor"))
    price = models.IntegerField()
    weight = models.IntegerField()
    Ingredients = models.TextField()

    class Meta:
        verbose_name ='Product'
        verbose_name_plural ='Products'
    
    def __str__(self):
        return self.name

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