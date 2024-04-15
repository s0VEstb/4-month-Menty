import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
class Post(models.Model):
    img = models.ImageField(upload_to='media/',null=True, blank=True)
    title = models.CharField(max_length=200, null=True)
    brand = models.CharField(max_length=255, null=True)
    model = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    year_of_issue = models.IntegerField(validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.date.today().year)
        ])
    text = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title