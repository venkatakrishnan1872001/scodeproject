from django.db import models

# Create your models here.

class Blog(models.Model):
    id=models.IntegerField(primary_key=True)
    blog_image = models.ImageField(upload_to='blog_images/', blank=True,null=True)
    title = models.CharField(max_length=255,blank=True,null=True)
    content =models.TextField()
    author_name =models.CharField(max_length=255,blank=True,null=True)
    created_by = models.CharField(max_length=255,blank=True,null=True)
    created_on =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"



class Scodedetail(models.Model):
    id=models.IntegerField(primary_key=True)
    image = models.ImageField(upload_to='bike_images/', blank=True,null=True) 
    heading = models.CharField(max_length=250,blank=True,null=True)
    para =  models.TextField()
    

    def __str__(self):
        return self.heading
