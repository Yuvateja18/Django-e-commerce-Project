from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name   #for displaying objects names



class Products(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='img', blank=True, null=True)

   

    @staticmethod
    def get_categoryid(category_id):

        if not category_id:
            return Products.objects.all()
        else:
            return Products.objects.filter(category=category_id)
        
    @staticmethod
    def get_by_category_id(category_id):
        if category_id:
            return Products.objects.filter(category=category_id)
        return Products.objects.all()
        
        
    def __str__(self):
        return self.name

from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=15, blank=True, null=True)
    password = models.CharField(max_length=28)  # Store hashed password

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
        



    
