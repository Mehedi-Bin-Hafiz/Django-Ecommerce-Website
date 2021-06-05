from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User,null= True, blank=True, on_delete=models.CASCADE) # one to one means user can only have customer, customer only have user
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200,null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True,blank=False)
    #image
    def __str__(self):
        return self.name

    
# Set the reference to NULL (requires the field to be nullable). For instance, when you delete a User, you might want to keep the comments he posted on blog posts, but say it was posted by an anonymous (or deleted) user. SQL equivalent: SET NULL.

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null= True, blank= True) #null=True , blank=True : This means that the field is optional in all circumstances # it is one to many relationship
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False) # complete filed initially uncomplete
    transaction_id = models.CharField(max_length=200, null=True)


    def __str__(self):
        return self.id


class OrderItem(models.Model):
    customer = models.ForeignKey(Product, on_delete=models.SET_NULL, null= True, blank= True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null= True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address






























