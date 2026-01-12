from django.shortcuts import redirect, render

from new_app.forms import ProductForm
from new_app.models import Seller


# product
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