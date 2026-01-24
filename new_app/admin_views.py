from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from new_app.filters import SellerFilter
from new_app.forms import CustomerForm, SellerForm
from new_app.models import Customer, Seller, BuyNow, Product


# admin base
@login_required(login_url='login_view')
def admin_base(request):
    return render(request,'admin/admin_base.html')

# read customer table
@login_required(login_url='login_view')
def read_customer(request):
    data = Customer.objects.all()
    return render(request,"admin/read_customer.html",{'data1':data})

# edit customer
@login_required(login_url='login_view')
def edit_customer(request,id):
    data = Customer.objects.get(id=id)
    form = CustomerForm(instance=data)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('read_customer')

    return render(request,'admin/edit_customer.html',{'form1':form})

# delete customer
@login_required(login_url='login_view')
def delete_customer(request,id):
    data = Customer.objects.get(id=id)
    data.delete()
    return redirect('read_customer')

# read seller
@login_required(login_url='login_view')
def read_seller(request):
    data = Seller.objects.all()
    return render(request,"admin/read_seller.html",{'data1':data})

# edit seller
@login_required(login_url='login_view')
def edit_seller(request,id):
    data = Seller.objects.get(id=id)
    form = SellerForm(instance=data)

    if request.method == 'POST':
        form = SellerForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('read_seller')

    return render(request,'admin/edit_seller.html',{'form1':form})

# delete seller
@login_required(login_url='login_view')
def delete_seller(request,id):
    data = Seller.objects.get(id=id)
    data.delete()
    return redirect('read_seller')

# buy now all
@login_required(login_url='login_view')
def all_order(request):
    data = BuyNow.objects.all()
    return render(request,"admin/all_buy_now.html",{'data1':data})

# products all
@login_required(login_url='login_view')
def all_product(request):
    product = Product.objects.all()
    sellerFilter = SellerFilter(request.GET, queryset=product)
    product = sellerFilter.qs
    context = {
        'product':product,
        'sellerFilter':sellerFilter
    }
    return render(request,"admin/all_product.html",context)
