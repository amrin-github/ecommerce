from django.contrib import admin

from new_app import models

# Register your models here.
admin.site.register(models.Seller)
admin.site.register(models.Customer)
admin.site.register(models.Login)
admin.site.register(models.Product)
admin.site.register(models.AddToCart)
admin.site.register(models.BuyNow)
