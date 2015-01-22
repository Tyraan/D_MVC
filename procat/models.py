from django.db import models



class Category(models.Model):
    name = models.CharField(max_length = 128)
    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length = 128)
    price = models.DecimalField(max_digits=10,decimal_places=3)
    uploadTime = models.DateTimeField(auto_now_add= True)
    description = models.CharField(max_length = 512)
    category = models.ManyToManyField(Category)
    def __str__(self):
        return self.name
    
    

