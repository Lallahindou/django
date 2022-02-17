from turtle import up
from django.db import models
from django.contrib.auth.models import User
#from django.db.models.signals import post_save
#from django.dispatch import receiver


class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name





class Book(models.Model):

    status_book = [
        ('availble','availble'),
        ('rental','rental'),
        ('sold','sold'),
    ]
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE) 
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    photo_book = models.ImageField(upload_to='photos',null=True,blank=True)
    photo_author = models.ImageField(upload_to='photos',null=True,blank=True)
    document = models.FileField(upload_to='doc',null=True,blank=True)
    pages = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    retal_price_day =  models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    retal_period = models.IntegerField(null=True, blank=True)
    total_rental = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices=status_book, null=True, blank=True)
    category = models.ForeignKey(Category,on_delete=models.PROTECT,null=True, blank=True)

    def __str__(self):
        return self.title

# Create your models here.
