# view product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from new_app.filters import ProductFilter
from new_app.forms import LoginRegister, CustomerForm, BuyNowForm
from new_app.models import Product, Customer, AddToCart, BuyNow, Seller


# customer base
@login_required(login_url='login_view')
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
@login_required(login_url='login_view')
def customer_profile(request):
    user_data = request.user
    # print(user_data.id)
    customer = Customer.objects.get(user=user_data)
    # print(customer.id)
    return render(request,'customer/customer_profile.html',{'customer1':customer})

# customer edit profile
@login_required(login_url='login_view')
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
@login_required(login_url='login_view')
def product_view(request):
    product = Product.objects.all()
    productFilter = ProductFilter(request.GET, queryset=product)
    product = productFilter.qs
    context = {
        'product':product,
        'productFilter':productFilter
    }
    return render(request,'customer/product_view.html',context)

# add to cart
@login_required(login_url='login_view')
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
    return redirect('view_cart')

# view cart
@login_required(login_url='login_view')
def view_cart(request):
    product_user = request.user
    customer_user = Customer.objects.get(user=product_user)
    product = AddToCart.objects.filter(user=customer_user)
    return render(request,'customer/view_cart.html',{'products':product})

# delete item from cart
@login_required(login_url='login_view')
def delete_item(request,id):
    data = AddToCart.objects.get(id=id)
    data.delete()
    return redirect('view_cart')

# buy
@login_required(login_url='login_view')
def buy_now(request, id):
    user = request.user
    customer = Customer.objects.get(user=user)
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = BuyNowForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if order.count > product.count:
                messages.info(request, "This product is not available.")
                return redirect('product_view')
            order.user = customer
            order.product = product
            order.save()
            product.count = product.count - order.count
            product.save()
            messages.success(request, 'Product has been ordered.')
            return redirect('order_list')
    else:
        form = BuyNowForm()

    return render(request,'customer/buy_now.html',{'form1':form,'product1':product})


# order list
@login_required(login_url='login_view')
def order_list(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    order = BuyNow.objects.filter(user=customer)
    return render(request,'customer/order_list.html',{'order1':order})

# add to cart buy now
@login_required(login_url='login_view')
def cart_buy_now(request,id):
    cart = AddToCart.objects.get(id=id)
    print(cart.product.count)
    if request.method == 'POST':
        form = BuyNowForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if order.count > cart.product.count:
                messages.info(request, "This product is not available.")
                return redirect('view_cart')
            order.user = cart.user
            order.product = cart.product
            order.save()
            cart.product.count = cart.product.count - order.count
            cart.product.save()
            messages.success(request, 'Product has been ordered.')
            return redirect('order_list')
    else:
        form = BuyNowForm()

    return render(request,'customer/cart_buy_now.html',{'form1':form,'cart':cart})






