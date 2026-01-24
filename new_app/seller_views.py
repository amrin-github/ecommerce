from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from new_app.forms import ProductForm, LoginRegister, SellerForm
from new_app.models import Seller, Product, BuyNow, Customer


# seller base
@login_required(login_url='login_view')
def seller_base(request):
    return render(request,'seller/seller_base.html')

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
            return redirect('login_view')

    return render(request,'seller/seller_form.html',{'form1':form1,'form2':form2})

# seller profile
@login_required(login_url='login_view')
def seller_profile(request):
    user_data = request.user
    # print(user_data.id)
    seller = Seller.objects.get(user=user_data)
    # print(seller.id)
    return render(request,'seller/seller_profile.html',{'seller1':seller})

# edit seller profile
@login_required(login_url='login_view')
def edit_seller_profile(request,id):
    data = Seller.objects.get(id=id)
    form = SellerForm(instance=data)
    if request.method == 'POST':
        form = SellerForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('seller_profile')
    return render(request,'seller/edit_seller_profile.html',{'form1':form})

# product
@login_required(login_url='login_view')
def product_upload(request):
    user_data = request.user
    seller = Seller.objects.get(user=user_data)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = seller
            data.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'seller/product_upload.html', {
        'form': form
    })



# filter product
@login_required(login_url='login_view')
def product_filter(request):
    product_user = request.user
    seller_user = Seller.objects.get(user=product_user)
    filter1 = Product.objects.filter(user=seller_user)
    return render(request,'seller/product_filter.html',{'filter1':filter1})

# delete product filter
@login_required(login_url='login_view')
def product_filter_delete(request,id):
    delete_product = Product.objects.get(id=id)
    delete_product.delete()
    return redirect('product_filter')

# edit product view
@login_required(login_url='login_view')
def product_filter_edit(request,id):
    data = Product.objects.get(id=id)
    form = ProductForm(instance=data)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect('product_filter')

    return render(request,'seller/product_filter_edit.html',{'form1':form})

# product order list
@login_required(login_url='login_view')
def product_order_list(request):
    product_user = request.user
    seller_user = Seller.objects.get(user=product_user)
    filter1 = BuyNow.objects.filter(product__user=seller_user)
    return render(request,'seller/product_order_list.html',{'filter1':filter1})
