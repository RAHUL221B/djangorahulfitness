from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self):
        return reverse('fatloss')


class Post(models.Model):
    sno= models.AutoField(primary_key=True)
    title= models.CharField(max_length=1800)
    title_tag = models.CharField(max_length=255)
    content= RichTextUploadingField(blank=True,null=True)
    author= models.CharField(max_length=230)
    slug= models.CharField(max_length=130)
    timestamp = models.DateTimeField(blank=True,null = True)
    category =  models.CharField(max_length=130, default = 'fatloss')
    header_image = models.ImageField(null=True,blank=True,upload_to="images/",default = "assets/21_duotone.png")
    snippet = models.CharField(max_length=255,default = 'Click the button below to view the entire Post')


    def __str__(self):
        return self.name
    
    def __str__(self):
        return self.title + 'by' + self.author

    def get_absolute_url(self):
        return reverse('fatlossPost',kwargs={"pk": self.pk})     
        # return ('fatlossPost',self.pk)