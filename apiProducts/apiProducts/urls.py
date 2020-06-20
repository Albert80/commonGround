from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from products import views

urlpatterns = [
    path('api/products', views.products_process),
    path('api/products/bulk_insert', views.products_process),
    path('admin/', admin.site.urls),
]