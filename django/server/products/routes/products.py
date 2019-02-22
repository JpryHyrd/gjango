from django.urls import path
from products.views import (
    RestProductListView
)


app_name = 'rest_products'

urlpatterns = [
    path('', RestProductListView.as_view(), name='list'),
]
