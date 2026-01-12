from django.urls import path

from new_app import views, seller_views

urlpatterns = [
    path("",views.home,name="home"),
    path("dashboard",views.dashboard,name="dashboard"),
    path("seller_form",views.seller_form,name="seller_form"),
    path("customer_form",views.customer_form,name="customer_form"),
    path("admin_base",views.admin_base,name="admin_base"),
    path("customer_base",views.customer_base,name="customer_base"),
    path("seller_base",views.seller_base,name="seller_base"),
    path("login_view",views.login_view,name="login_view"),
    path("read_customer",views.read_customer,name="read_customer"),
    path("edit_customer/<int:id>",views.edit_customer,name="edit_customer"),
    path("delete_customer/<int:id>",views.delete_customer,name="delete_customer"),
    path("read_seller", views.read_seller, name="read_seller"),
    path("edit_seller/<int:id>", views.edit_seller, name="edit_seller"),
    path("delete_seller/<int:id>", views.delete_seller, name="delete_seller"),
    path("seller_profile", views.seller_profile, name="seller_profile"),
    path("edit_seller_profile/<int:id>", views.edit_seller_profile, name="edit_seller_profile"),
    path("customer_profile", views.customer_profile, name="customer_profile"),
    path("edit_customer_profile/<int:id>", views.edit_customer_profile, name="edit_customer_profile"),
    path("product_upload", seller_views.product_upload, name="product_upload"),

]