from django.urls import path, include
import products.views as products
from products.views import contacts_prod, index_prod
from products.views import (product_detail_view, index_prod, product_create_view, product_update_view, product_delete_view,
        ProductListView, ProductDetailView, ProductCreateView, ProductUdateView, ProductDeleteView)
#from products.views import category_create_view
#from products.views import category_update_view
#from django.conf import settings
#from django.conf.urls.static import static


#app_name = "products"


urlpatterns = [
    path("", ProductListView.as_view(), name="list"),
#    path("prd/", contacts_prod),

    path('mdir/', products.products, name='index'),
    path('categor/<int:pk>/', products.products, name='category'),

    path("<int:pk>", ProductDetailView.as_view(), name="detail"),
    path("create/", ProductCreateView.as_view(), name="create"),
    path("<int:pk>/update/", ProductUdateView.as_view(), name="update"),
    path("<int:pk>/delete/", ProductDeleteView.as_view(), name="delete"),
    path("<int:pk>", index_prod, name="detail"),
    #path("categories/create/", category_create_view, name="create"),
    #path("categories/<int:pk>/update/", category_update_view, name="update"),
    #path('accounts/', include('allauth.urls')),

]