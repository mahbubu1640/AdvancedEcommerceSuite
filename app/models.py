from django.db import models
from django.contrib.auth.models import User

# user/name / locality /city /zipcode / state 


STATE_CHOICES = (
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh ', 'Arunachal Pradesh '),
    ('Assam ','Assam'),
    ('Bihar','Bihar'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat'),
    ('Haryana','Haryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Telangana','Telangana'),
    ('Tripura','Tripura'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('Uttarakhand','Uttarakhand'),
    ('West Bengal','West Bengal'),
)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    locality = models.CharField(max_length=64)
    city = models.CharField(max_length=54)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES ,max_length=25)
    
    
    def __str__(self):
        return str(self.id)

#  title / selling price /discounted price / description /brand /category / product images
# Mobile/Laptop/Bottom Wear / Top Wear
PRODUCT_CHOICES = (
    ('Mobile','Mobile'),
    ('Laptop','Laptop'),
    ('Bottom Wear','Bottom Wear'),
    ('Top Wear','Top Wear'),
)



class Product(models.Model):
    title = models.CharField(max_length=64)
    selling_price = models.PositiveIntegerField()
    discounted_price = models.PositiveIntegerField()
    description = models.TextField()
    brand = models.CharField(max_length=64)
    category = models.CharField(choices =PRODUCT_CHOICES ,max_length=11)
    product_images=models.ImageField(upload_to='procudtimg') 
    def __str__(self):
        return str(self.id)
#User / product /quantity 


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return str(self.id)

# user/customer/product /quantity /ordered_date/status/
# Accepted/packed/On The Way /Delivered/Cancel/
OrderPlaced_CHOICES =(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices =OrderPlaced_CHOICES , max_length=10)
    