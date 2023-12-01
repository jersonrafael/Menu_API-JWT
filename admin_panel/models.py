from django.db import models

# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class plate(models.Model):
    name = models.CharField(max_length=255, null=False)
    price = models.FloatField()
    ingredient = models.TextField()

    image = models.ImageField(upload_to='static/', blank=True,null=True)

    category = models.ForeignKey(category,default=0,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class drink(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    img = models.ImageField(upload_to="static/",blank=True,null=True)

    def __str__(self):
        return self.name