from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50)
    category=models.ForeignKey('Category',on_delete=models.CASCADE)
    description=models.TextField(max_length=200)
    price=models.PositiveIntegerField()
    inventory=models.PositiveIntegerField()
    brand=models.ForeignKey('Brand',on_delete=models.CASCADE)
    image=models.ImageField(upload_to='products/',default='products/default.jpg',null=True,blank=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering=('name','price',)    
    def get_absolute_url(self):
        return reverse('product-detail',args=[str(self.id)])
class Brand(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    class Meta:
        ordering=('name',)
    def get_absolute_url(self):
        return reverse('brand-detail',args=[str(self.id)])

class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    class Meta:
        ordering=('name',)
    def get_absolute_url(self):
        return reverse('category-detail',args=[str(self.id)])

class CartItem(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    @property
    def total_price(self):
        return self.product.price * self.quantity