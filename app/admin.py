from django.contrib import admin
from .models import Customer,Product,Cart,OrderPlaced
# Register your models here.
# customer/product / cart / orderplaced 
 
# user/name / locality /city /zipcode / state 


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ["id","user","name","locality","city","zipcode","state"]

#  title / selling price /discounted price / description /brand /category / product images
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ["id","title","selling_price","discounted_price","description","brand","category","product_images"]
    
@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display=["id","user","product","quantity"]

# user/customer/product /quantity /ordered_date/status/
@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ["id","user","customer","product","quantity","ordered_date","status"]
