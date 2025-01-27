from django.urls import path
from . import views
from catalog.views import index, contact, product_detail, home


app_name = 'catalog'

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contact, name='contacts'),
    path('product/<int:pk>', views.product_detail, name='product')
]