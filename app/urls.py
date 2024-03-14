from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import (LoginForm,MyPasswordChangeForm,
        MyPasswordResetForm,MyPasswordSetForm)

urlpatterns = [
    path('', views.ProductView.as_view(),name='home'),
    path('add_product/', views.ProductCreateView.as_view(), name='add_product'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    #path('cart/', views.add_to_cart, name='add-to-cart'),
    path('add_to_cart/', views.add_to_cart, name='add-to-cart'),
    path('show_cart/', views.show_cart, name='show-cart'),
    path('plus_cart/',views.plus_cart, name='plus-cart'),
    path('minus_cart/',views.minus_cart, name='minus-cart'),
    path('remove_cart/',views.remove_cart, name='remove-cart'),
    
    path('buy/', views.buy_now, name='buy-now'),
    #path('profile/', views.profile, name='profile'),
    
    path('profile/', views.ProfileView.as_view(), name='profile'),
    
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    # path('changepassword/', views.change_password, name='changepassword'),
    path('password_reset/', views.password_reset, name='password_reset'),
    #path('mobile/', views.mobile, name='mobile'),
    path('mobile/', views.MobileListView.as_view(), name='mobile'),
    path('mobile/<slug:data>', views.MobileListView.as_view(), name='mobiledata'),
    path('laptop/', views.LaptopListView.as_view(), name='laptop'),
    path('laptop/<slug:data>', views.LaptopProductView.as_view(), name='laptopdata'),
    path('login/', views.login, name='login'),
    
    path('accounts/login/', auth_view.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm),name="login"),
    
    path('logout/', auth_view.LogoutView.as_view(next_page='login'),name="logout"),

    path('passwordchange/',auth_view.PasswordChangeView.as_view(template_name
    ='app/passwordchange.html',form_class=MyPasswordChangeForm,
    success_url='/passwordchangedone/'),name='passwordchange'),
    
    path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name
    ='app/passwordchangedone.html'),name='passwordchangedone'),
    
    path('password-reset',auth_view.PasswordResetView.as_view(template_name="app/password_reset.html"
    ,form_class=MyPasswordResetForm),name="password_reset"),
    
    path('password_reset/done/',auth_view.PasswordResetDoneView.as_view(template_name
    ='app/password_reset_done.html'),name='password_reset_done'),
    
    path('password_reset_confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name=
    "app/password_reset_confirm.html",form_class=MyPasswordSetForm),
    name="password_reset_confirm"),
    
    path('password_reset_complete',auth_view.PasswordResetCompleteView.as_view(template_name
    ='app/password_reset_complete.html'),name='password_reset_complete'),
    
    
    
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

#+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
 