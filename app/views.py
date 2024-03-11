from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView
from .models import Product
from django.urls import reverse_lazy
# Change this view into create class based view 
# -- to pass Top wear , Bottom wear , Mobile , Laptop  into template contex/render
# -- filter it by category and display it to the homepage by category type 
# -- create url for View 
# home(request)
# - this view is only displaying html static images / not from the database or filter // 


# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
    def get(self,request):
        topwears = Product.objects.filter(category='Top Wear')
        bottomwears = Product.objects.filter(category='Bottom Wear')
        mobiles = Product.objects.filter(category='Mobile')
        laptop = Product.objects.filter(category = 'Laptop')
        return render(request,'app/home.html',{'topwears':topwears,
            'bottomwears':bottomwears,'mobiles':mobiles,'laptop':laptop})

class ProductCreateView(CreateView):
    model = Product 
    fields = ['title','selling_price','discounted_price','description','brand','category','product_images',]
    template_name = 'add_product.html'
    success_url = reverse_lazy('home')


# def product_detail(request):
#  return render(request, 'app/productdetail.html')

# def product_detail(request,pk):
#     product=Product.objects.get(pk=pk)
#     return render(request,'app/productdetail.html',{'product':product})



class ProductDetailView(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,'app/productdetail.html',{'product':product})

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

class MobileListView(View):
    def get(self,request):
        mobile = Product.objects.filter(category='Mobile')
        return render(request,'app/mobile.html',{'mobile':mobile})

class LaptopListView(View):
    def get(self,request):
        laptop = Product.objects.filter(category='Laptop')
        return render(request,'app/laptop.html',{'laptop':laptop})


def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
