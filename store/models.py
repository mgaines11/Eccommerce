from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model): 
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    # slugField is behind the scenes ensuring that the category isn't repeated or attempted with special characters (!@#$%)

    class Meta:
        verbose_name_plural = 'categories'
        # by default django will change class category to categorys 
        # this func allows to override that setting in the admin area
    
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)
        # will return what item was added to the data base in descending order
        # leaving first item added to the database at the bottom 
    
    def __str__(self):
        return self.title