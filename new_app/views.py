from urllib import request

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from new_app.models import Product


# Create your views here.
# main page
def home(request):
    product = Product.objects.all()
    return render(request,'home.html',{'product':product})

# dashboard
def dashboard(request):
    return render(request,'dashboard.html')

# login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        # print(username)
        password = request.POST.get('pass')
        # print(password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('admin_base')
            if user.is_customer:
                return redirect('customer_base')
            if user.is_seller:
                return redirect('seller_base')
        else:
            print('Invalid username or password')
    return render(request,'login.html')

# logout
def logout_view(request):
    logout(request)
    return redirect('home')







