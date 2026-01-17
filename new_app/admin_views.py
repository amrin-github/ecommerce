
from django.shortcuts import render, redirect

from new_app.forms import CustomerForm, SellerForm
from new_app.models import Customer, Seller, BuyNow


# admin base
def admin_base(request):
    return render(request,'admin/admin_base.html')

# read customer table
def read_customer(request):
    data = Customer.objects.all()
    return render(request,"admin/read_customer.html",{'data1':data})

# edit customer
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
def delete_customer(request,id):
    data = Customer.objects.get(id=id)
    data.delete()
    return redirect('read_customer')

# read seller
def read_seller(request):
    data = Seller.objects.all()
    return render(request,"admin/read_seller.html",{'data1':data})

# edit seller
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
def delete_seller(request,id):
    data = Seller.objects.get(id=id)
    data.delete()
    return redirect('read_seller')

# buy now all
def all_order(request):
    data = BuyNow.objects.all()
    return render(request,"admin/all_buy_now.html",{'data1':data})
