from django.shortcuts import render, redirect, get_object_or_404
from django.template import Template, Context
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string
import json
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from products.models import Product, Category
#from products.forms import CategoryForm, CategoryModelForm, ProductForm
from products.forms import ProductForm
from django.urls import reverse, reverse_lazy
from django.http import Http404, JsonResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 


class RestProductListView(ListView):
    model = Product
    template_name = 'products/index.html'
    paginate_by = 2

    def serialize_object_list(self, queryset):
        return list(
            map(
                lambda itm: {
                    'id': itm.id,
                    'name': itm.name,
                    'category': itm.category.name if itm.category else None,
                    'image': itm.image.url if itm.image else None,
                    'cost': itm.cost
                },
                queryset
            )
        )

    def get_context_data(self, **kwargs):
        context = super(RestProductListView, self).get_context_data(**kwargs)

        data = {}
        page = context.get('page_obj')
        route_url = reverse('rest_products:list')

        data['next_url'] = None
        data['previous_url'] = None
        data['page'] = page.number
        data['count'] = page.paginator.count
        data['results'] = self.serialize_object_list(page.object_list)

        if page.has_previous():
            data['previous_url'] = f'{route_url}?page={page.previous_page_number()}'

        if page.has_next():
            data['next_url'] = f'{route_url}?page={page.next_page_number()}'

        return data

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)



class ProductListView(ListView):
        model = Product
        template_name = 'products/index.html'

        paginate_by = 1
"""        def get_context_data(self, **kwargs):
                context = super(ProductListView, self).get_context_data(**kwargs)
                queryset = context.get("object_list")
                page = self.request.GET.get("page")
                paginator = Paginator(queryset, 1)
                page_obj = paginator.get_page(page)

                context["page_obj"] = page_obj
                return context"""


class ProductDetailView(DetailView):
        model = Product
        template_name = 'products/detail.html'
        context_object_name = 'inst'


class ProductCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
        model = Product
        form_class = ProductForm
        template_name = 'products/create.html'
#    success_url = reverse_lazy('products:list')
        success_url = reverse_lazy('list')
        login_url = reverse_lazy('accounts:login')

        def test_func(self):
                return self.request.user.has_perm('products.add_product')


class ProductUdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
        model = Product
        fields = [
                'name', 'image', 'category',
                'description', 'cost'
        ]
        template_name = 'products/create.html'
        success_url = reverse_lazy('list')
        login_url = reverse_lazy('accounts:login')
#    success_url = reverse_lazy('products:list')
        def test_func(self):
                return self.request.user.has_perm('products.change_product')




class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
        model = Product
        template_name = 'products/delete.html'
#        success_url = reverse_lazy('products:list')
        success_url = reverse_lazy('list')
        login_url = reverse_lazy('accounts:login')
        def test_func(self):
                return self.request.user.is_superuser


def contacts_prod(request):
        with open("products/fixtures/data/data.json") as file:
                data = json.load(file)
                return render(request, "products/contacts.html", {"object_list" : data})

def index_prod(request):
        #with open("products/fixtures/data/data.json") as file:
        #        data = json.load(file)
        data = Product.objects.all()
        return render(request, "products/index.html", {"object_list" : data})

def product_detail_view(request, pk):
        #with open("products/fixtures/data/data.json") as file:
        #data = json.load(file)
        data = Product.objects.get(pk = pk)
        return render(request,"products/detail.html", {"inst" : data})
                #return render(request,"products/detail.html", {"object" : data[idx]})



@login_required(login_url=reverse_lazy('accounts:login'))
def product_create_view(request):
        form = ProductForm()
        success_url = reverse("list")
        if request.method == "POST":
                form = ProductForm(data = request.POST)
                if form.is_valid():
                        form.save()
        return render(request, "products/create.html", {"form":form})

@login_required(login_url=reverse_lazy('accounts:login'))
def product_update_view(request, pk):
        obj = get_object_or_404(Product, pk=pk)

        form = ProductForm(instance = obj)
        success_url = reverse("list")
        
        if request.method == "POST":
                form = ProductForm(data = request.POST, files = request.FILES, instance = obj)
                if form.is_valid():
                        form.save()
                        return redirect(success_url)
        return render(request, "products/update.html", {"form":form})

@login_required(login_url=reverse_lazy('accounts:login'))
def product_delete_view(request, pk):
        obj = get_object_or_404(Product, pk=pk)
        success_url = reverse("list")
        if request.method == "POST":
                obj.delete()
                return redirect(success_url)
        return render(request, "products/delete.html", {'object':obj})
      
        
def products(request, pk=None):
        print(pk)
    
        title = 'Products'
        links_menu = Category.objects.all()
            
        if pk is not None:
                if pk == 0:
                        products = Product.objects.all().order_by('price')
                        category = {'name': 'все'}
                else:
                        category = get_object_or_404(Category, pk=pk)
                products = Product.objects.filter(category__pk=pk).order_by('price')

                content = {
                'title': title,
                'links_menu': links_menu,
                'category': category,
                'products': products,
                }

                return render(request, 'products/index.html', content)

    
        same_products = Product.objects.all()[3:5]
    
        content = {
                'title': title, 
                'links_menu': links_menu, 
                'same_products': same_products
        }
    
        return render(request, 'products/products.html', content)

def Basket(request, pk):
        basket = []
        if request.user.is_authenticated:
                basket = Basket.objects.filter(user=request.user)
            
        if pk:
                if pk == '0':
                        products = Product.objects.all().order_by('price')
                        category = {'name': 'все'}
                else:
                        category = get_object_or_404(ProductCategory, pk=pk)
                        products = Product.objects.filter(category__pk=pk).order_by('price')
        
                content = {
                'title': title,
                'links_menu': links_menu,
                'category': category,
                'products': products,
                'basket': basket,
                }
        
                return render(request, 'mainapp/products_list.html', content)




