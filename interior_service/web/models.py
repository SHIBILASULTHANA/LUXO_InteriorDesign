from django.db import models
from django.urls import reverse

# Create your models here.

class Team(models.Model):
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)

class Testimonial(models.Model):
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    name = models.CharField(max_length=50)
    job = models.CharField(max_length=80)
    quote = models.TextField()

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    category_description = models.TextField()
    category_title = models.CharField(max_length=250)
    category_image = models.ImageField(upload_to='media/',null=True ,blank=True)
    related_image1 = models.ImageField(upload_to='media/',null=True ,blank=True)
    related_image2 = models.ImageField(upload_to='media/',null=True ,blank=True)
    related_image3 = models.ImageField(upload_to='media/',null=True ,blank=True)

    def __str__(self):
        return self.category_name
    
class Services(models.Model):
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/', null=True, blank=True)

    def __str__(self):
        return self.title
    
class Blog(models.Model):
    profile_image = models.ImageField(upload_to='media')
    title = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    category_choices = [
        ('Interior','Interior'),('Building','Building'),('Architecture','Architecture')
    ]
    category = models.CharField(max_length=20, choices=category_choices, default='Interior')
    description = models.TextField()
    detail_image = models.ImageField(upload_to='media')
    related_image1 = models.ImageField(upload_to='media')
    related_image2 = models.ImageField(upload_to='media')

    def __str__(self):
        return self.title
    