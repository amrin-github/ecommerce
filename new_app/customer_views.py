# view product
from django.contrib import messages
from django.shortcuts import render, redirect

from new_app.forms import LoginRegister, CustomerForm, BuyNowForm
from new_app.models import Product, Customer, AddToCart, BuyNow, Seller


# customer base
def customer_base(request):
    return render(request,'customer/customer_base.html')

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
            return redirect('login_view')

    return render(request,'customer/customer_form.html',{'form3':form1,'form4':form2})

# customer profile
def customer_profile(request):
    user_data = request.user
    # print(user_data.id)
    customer = Customer.objects.get(user=user_data)
    # print(customer.id)
    return render(request,'customer/customer_profile.html',{'customer1':customer})

# customer edit profile
def edit_customer_profile(request,id):
    data = Customer.objects.get(id=id)
    form = CustomerForm(instance=data)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('customer_profile')
    return render(request,'customer/edit_customer_profile.html',{'form1':form})


# product view
def product_view(request):
    product = Product.objects.all()
    return render(request,'customer/product_view.html',{'products':product})

# add to cart
def add_to_cart(request,id):
    customer = request.user
    customer_data = Customer.objects.get(user=customer)
    product = Product.objects.get(id=id)
    data = AddToCart.objects.filter(user=customer_data,product=product)
    if data.exists():
        messages.info(request,'Product already added to cart.')
    else:
        AddToCart.objects.create(user=customer_data,product=product)
        messages.success(request,'Product added to cart.')
    return redirect('product_view')

# view cart
def view_cart(request):
    product_user = request.user
    customer_user = Customer.objects.get(user=product_user)
    product = AddToCart.objects.filter(user=customer_user)
    return render(request,'customer/view_cart.html',{'products':product})

# delete item from cart
def delete_item(request,id):
    data = AddToCart.objects.get(id=id)
    data.delete()
    return redirect('view_cart')

# buy
def buy_now(request, id):
    user = request.user
    customer = Customer.objects.get(user=user)
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = BuyNowForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = customer
            order.product = product
            order.save()
            return redirect('view_cart')
    else:
        form = BuyNowForm()

    return render(request,'customer/buy_now.html',{'form1':form,'product1':product})


# order list
def order_list(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    order = BuyNow.objects.filter(user=customer)
    return render(request,'customer/order_list.html',{'order1':order})





