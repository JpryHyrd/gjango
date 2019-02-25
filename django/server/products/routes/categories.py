"""from django.urls import path, include
#from products.views import contacts_prod, index_prod
#from products.views import (product_detail_view, index_prod)
from products.views import category_create_view, CategoryListView, CategoryDetailView, CategoryCreateView, CategoryUdateView, CategoryDeleteView
from products.views import category_update_view
#from django.conf import settings
#from django.conf.urls.static import static


#app_name = "categories"


urlpatterns = [
    #path("", index_prod, name="list"),
    #path("prd/", contacts_prod),
    #path("<int:pk>", product_detail_view, name="detail"),
    #path("<int:pk>", index_prod, name="detail"),
    path("create/", CategoryCreateView.as_view(), name="create"),
    path("<int:pk>/update/", CategoryUdateView.as_view(), name="update"),
    path("", CategoryListView.as_view(), name="list"),
    path("<int:pk>", CategoryDetailView.as_view(), name="detail"),
    path("<int:pk>/delete", CategoryDeleteView.as_view(), name="delete"),

    #path('accounts/', include('allauth.urls')),

]"""
from django.urls import path
from products.views import (
    RestCategoryListView
)


app_name = 'rest_categories'

urlpatterns = [
    path('', RestCategoryListView.as_view(), name='list'),
]
