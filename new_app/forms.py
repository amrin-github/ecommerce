from xml.dom.minidom import Document

from django import forms
from django.contrib.auth.forms import UserCreationForm

from new_app.models import Login, Seller, Customer, Product, BuyNow


# login
class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label= "password",widget=forms.PasswordInput)
    password2 = forms.CharField(label= "confirm password",widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username','password1','password2')


# seller
class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ('GST_no','name','email','phone_number','address')


# customer
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
        exclude = ('user',)

# product
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name','price','count','seller_image',)

# buy now
class BuyNowForm(forms.ModelForm):
    class Meta:
        model = BuyNow
        fields = '__all__'
        exclude = ('user','product','status',)

