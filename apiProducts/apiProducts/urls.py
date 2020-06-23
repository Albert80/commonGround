from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
# from products import views
from products import api

urlpatterns = [
    # path('api/products', views.products_process),
    # path('api/products/bulk_insert', views.products_process),
    path('api/products', api.ProductAPI.as_view({'get': 'list'})),
    path('api/products/bulk_insert', api.ProductAPI.as_view({'post': 'create'})),
    path('admin/', admin.site.urls),
]

urlpatterns = format_suffix_patterns(urlpatterns)