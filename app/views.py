from django.shortcuts import render,redirect
from django.views import View
from django.views.generic.edit import CreateView

from .models import Product
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import CustomerProfileForm
from .models import Customer,Cart
from .forms import CustomRegistrationForm
from django.db.models import Q
from django.http import JsonResponse


def password_reset(request):
    pass


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




class ProductDetailView(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,'app/productdetail.html',{'product':product})

def show_cart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        print(cart)
        amount=0.0
        shiping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user==user]
        print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamount=(p.quantity * p.product.discounted_price)
                amount+=tempamount
            totalamount=amount+shiping_amount
                
            return render(request,'app/addtocart.html',{'carts':cart,
            'totalamount':totalamount,'amount':amount})
        else:
            return render(request,"app/emptycart.html")

from django.http import JsonResponse
from django.db.models import Q

def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')  # Use get() method to avoid KeyError
        print(prod_id)
        try:
            c = Cart.objects.get(product=prod_id, user=request.user)
            c.quantity += 1
            c.save()
            amount = 0.00
            shiping_amount = 70.00
            cart_product = Cart.objects.filter(user=request.user)
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
            #totalamount = amount + shiping_amount
            data = {
                'quantity': c.quantity,
                'amount': amount,
                'totalamount': amount+shiping_amount
            }
            return JsonResponse(data)
        except Cart.DoesNotExist:
            return JsonResponse({'error': 'Cart item does not exist'})

def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')  # Use get() method to avoid KeyError
        print(prod_id)
        try:
            c = Cart.objects.get(product=prod_id, user=request.user)
            c.quantity -= 1
            c.save()
            amount = 0.00
            shiping_amount = 70.00
            cart_product = Cart.objects.filter(user=request.user)
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
            #totalamount = amount + shiping_amount
            data = {
                'quantity': c.quantity,
                'amount': amount,
                'totalamount': amount+shiping_amount
            }
            return JsonResponse(data)
        except Cart.DoesNotExist:
            return JsonResponse({'error': 'Cart item does not exist'})

def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET.get('prod_id')  # Use get() method to avoid KeyError
        print(prod_id)
        try:
            c = Cart.objects.get(product=prod_id, user=request.user)
            c.delete()
            amount = 0.00
            shiping_amount = 70.00
            cart_product = Cart.objects.filter(user=request.user)
            for p in cart_product:
                tempamount = (p.quantity * p.product.discounted_price)
                amount += tempamount
            totalamount = amount + shiping_amount
            data = {
                'amount': amount,
                'totalamount': totalamount
            }
            return JsonResponse(data)
        except Cart.DoesNotExist:
            return JsonResponse({'error': 'Cart item does not exist'})


def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    print(product_id)
    return redirect('/show_cart')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
    # add= Customer.objects.filter(user=request.user)
    address=Customer.objects.all()
    return render(request, 'app/address.html',{'address':address}) #{'add':add})

def orders(request):
 return render(request, 'app/orders.html')

# def change_password(request):
#  return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

class MobileListView(View):
    def get(self,request,data=None):
        if data is None:
            mobile = Product.objects.filter(category='Mobile')
        elif data =="Redmi" or data =="Samsung":
            mobile = Product.objects.filter(category="Mobile",brand=data)
        elif data == "below":
            mobile = Product.objects.filter(category="Mobile",discounted_price__lt=10000)
        elif data =="above":
            mobile = Product.objects.filter(category="Mobile",discounted_price__gt=10000)
        return render(request,'app/mobile.html',{'mobile':mobile})

class LaptopListView(View):
    def get(self,request):
        laptop = Product.objects.filter(category='Laptop')
        return render(request,'app/laptop.html',{'laptop':laptop})
    
class LaptopProductView(View):
    def get(self,request,data=None):
        if data is None:
            laptop = Product.objects.filter(category="Laptop")
        elif data =="Hp" or data == "MSI":
            laptop = Product.objects.filter(category="Laptop",brand=data)
        elif data =="above":
            laptop = Product.objects.filter(category="Laptop",discounted_price__gt=20000)
        elif data == "below":
            laptop = Product.objects.filter(category="Laptop",discounted_price__lt=20000)
        
        return render(request,'app/laptop.html',{'laptop':laptop})
        
    

def login(request):
 return render(request, 'app/login.html')




class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomRegistrationForm()
        return render(request,"app/customerregistration.html",{'form':form})
    def post(self,request):
        form= CustomRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,"Congratulations ! Registered Successfully")
            form.save()
        return render(request,"app/customerregistration.html",{'form':form})
        
    
def checkout(request):
 return render(request, 'app/checkout.html')


class ProfileView(View):
    def get(self,request):
        form =CustomerProfileForm()
        return render(request,"app/profile.html",{'form':form,
        'active':'btn-primary'})
    
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=usr,name=name,locality=locality,
            city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,'Congratulations!! Profile Updated Successfully')
        return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})
