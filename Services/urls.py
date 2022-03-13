from django.urls import path, include
from .views import Home, ServiceView,ReviewView,EditProduct,DeleteProduct,AddProduct,AddproductType

urlpatterns = [
    path("",Home,name="home"),
    path("service", ServiceView,name="service"),
    path("review/",ReviewView,name="review"),
    path("product-type/",AddproductType, name="product_type"),
    path("add-product/", AddProduct, name="add-product"),
    path("product/<int:id>/edit", EditProduct,name="product-edit"),
    path("product/<int:id>/delete", DeleteProduct,name="product-delete"),

    ]