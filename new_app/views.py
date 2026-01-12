from urllib import request

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from new_app.forms import LoginRegister, SellerForm, CustomerForm
from new_app.models import Customer, Seller


# Create your views here.
# main page
def home(request):
    return render(request,'home.html')

# dashboard
def dashboard(request):
    return render(request,'dashboard.html')

# seller
def seller_form(request):
    form1 = LoginRegister()
    form2 = SellerForm()

    if request.method == 'POST':
        form3 = LoginRegister(request.POST)
        form4 = SellerForm(request.POST)
        if form3.is_valid() and form4.is_valid():
            data1 = form3.save(commit = False)
            data1.is_seller = True
            data1.save()

            data2 = form4.save(commit=False)
            data2.user = data1
            data2.save()

    return render(request,'seller_form.html',{'form1':form1,'form2':form2})

# customer
def customer_form(request):
    form1 = LoginRegister()
    form2 = CustomerForm()

    if request.method == 'POST':
        form3 = LoginRegister(request.POST)
        form4 = CustomerForm(request.POST)
        if form3.is_valid() and form4.is_valid():
            data3 = form3.save(commit = False)
            data3.is_customer = True
            data3.save()

            data4 = form4.save(commit=False)
            data4.user = data3
            data4.save()

    return render(request,'customer_form.html',{'form3':form1,'form4':form2})

# read customer table
def read_customer(request):
    data = Customer.objects.all()
    return render(request,"read_customer.html",{'data1':data})

# edit customer
def edit_customer(request,id):
    data = Customer.objects.get(id=id)
    form = CustomerForm(instance=data)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('read_customer')

    return render(request,'edit_customer.html',{'form1':form})

# delete customer
def delete_customer(request,id):
    data = Customer.objects.get(id=id)
    data.delete()
    return redirect('read_customer')

# read seller
def read_seller(request):
    data = Seller.objects.all()
    return render(request,"read_seller.html",{'data1':data})

# edit seller
def edit_seller(request,id):
    data = Seller.objects.get(id=id)
    form = SellerForm(instance=data)

    if request.method == 'POST':
        form = SellerForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('read_seller')

    return render(request,'edit_seller.html',{'form1':form})

# delete seller
def delete_seller(request,id):
    data = Seller.objects.get(id=id)
    data.delete()
    return redirect('read_seller')

# admin base
def admin_base(request):
    return render(request,'admin/admin_base.html')

# customer base
def customer_base(request):
    return render(request,'customer/customer_base.html')

# seller base
def seller_base(request):
    return render(request,'seller/seller_base.html')

# login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        print(username)
        password = request.POST.get('pass')
        print(password)
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

# seller profile
def seller_profile(request):
    user_data = request.user
    # print(user_data.id)
    seller = Seller.objects.get(user=user_data)
    # print(seller.id)
    return render(request,'seller_profile.html',{'seller1':seller})

# edit seller profile
def edit_seller_profile(request,id):
    data = Seller.objects.get(id=id)
    form = SellerForm(instance=data)
    if request.method == 'POST':
        form = SellerForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('seller_profile')
    return render(request,'edit_seller_profile.html',{'form1':form})

# customer profile
def customer_profile(request):
    user_data = request.user
    # print(user_data.id)
    customer = Customer.objects.get(user=user_data)
    # print(customer.id)
    return render(request,'customer_profile.html',{'customer1':customer})

# customer edit profile
def edit_customer_profile(request,id):
    data = Customer.objects.get(id=id)
    form = CustomerForm(instance=data)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('customer_profile')
    return render(request,'edit_customer_profile.html',{'form1':form})



