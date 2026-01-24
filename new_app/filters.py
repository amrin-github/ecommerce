import django_filters
from django import forms
from django_filters import CharFilter

from new_app.models import Product

# product filter search
class ProductFilter(django_filters.FilterSet):
    name = CharFilter(label='',lookup_expr='icontains',widget=forms.TextInput(attrs={
        'placeholder':'Search','class':'form-control'}))

    class Meta:
        model = Product
        fields = ('name',)

# seller search
class SellerFilter(django_filters.FilterSet):
    user__name = CharFilter(label='',lookup_expr='icontains',widget=forms.TextInput(attrs={
        'placeholder':'Search','class':'form-control'}))

    class Meta:
        model = Product
        fields = ('user__name',)


