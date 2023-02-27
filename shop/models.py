from django.db import models

# Create your models here.

class categ(models.Model):
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)


    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    price = models.IntegerField()
    desc = models.TextField()
    image = models.ImageField(upload_to='picture')
    available = models.BooleanField()
    stock = models.IntegerField()
    category = models.ForeignKey(categ, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


