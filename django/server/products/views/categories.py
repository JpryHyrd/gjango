from django.shortcuts import render, redirect
from django.template import Template, Context
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string
import json
from products.models import Product, Category
from products.forms import CategoryForm, CategoryModelForm
from django.urls import reverse, reverse_lazy
from django.http import Http404, JsonResponse
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.core.paginator import Paginator

 
class RestCategoryListView(ListView):
    model = Category

    def serialize_object_list(self, queryset):
        return list(
            map(
                lambda itm: {
                    'id': itm.id,
                    'name': itm.name
                },
                queryset
            )
        )

    def get_context_data(self, **kwargs):
        context = super(RestCategoryListView, self).get_context_data(**kwargs)
        object_list = context.get('object_list')

        data = {}
        data['results'] = self.serialize_object_list(object_list)

        return data

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)


class CategoryListView(ListView):
        model = Category
        template_name = 'categories/index.html'


class CategoryDetailView(DetailView):
        model = Category
        template_name = 'categories/detail.html'
#       context_object_name = 'inst'

"""        def get_context_data(self, **kwargs):
                key = self.context_object_name if self.context_object_name else "object"
                obj = kwargs.get(key)
                products = obj.product_set.all()
                page = self.request.GET.get("page")
                paginator = Paginator(products, 1)
                page_obj = paginator.get_page(page)

                return{ key:obj, "products":page_obj }"""


class CategoryCreateView(CreateView):
        model = Category
        form_class = CategoryModelForm
        template_name = 'categories/create.html'
#    success_url = reverse_lazy('categories:list')
        success_url = reverse_lazy('list')


class CategoryUdateView(UpdateView):
        model = Category
        form_class = CategoryModelForm
        template_name = 'categories/create.html'
        success_url = reverse_lazy('list')
#    success_url = reverse_lazy('categories:list')



class CategoryDeleteView(DeleteView):
        model = Category
        template_name = 'categories/delete.html'
#        success_url = reverse_lazy('categories:list')
        success_url = reverse_lazy('list')

"""def contacts_prod(request):
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
        return render(request,"products/detail.html", {"object" : data})
                #return render(request,"products/detail.html", {"object" : data[idx]})"""
def category_create_view(request):
        form = CategoryModelForm()
        success_url = reverse("list")
        if request.method == "POST":
                form = CategoryModelForm(data = request.POST)
                if form.is_valid():
                        form.save()
                        #obj = Category(name = form.cleaned_data.get("name"), description = form.cleaned_data.get("description"))
                        #obj.save()
                        #return redirect(success_url)
        return render(request, "categories/create.html", {"form":form})
def category_update_view(request, pk):
        try:
                obj = Category.object.get(pk=pk)
        except Exception as err:
                raise Http404
        form = CategoryModelForm(instance = obj)
        success_url = reverse("list")
        
        if request.method == "POST":
                form = CategoryModelForm(request.POST, files = request.FILES, initial = obj)
                if form.is_valid():
                        form.save()
                        return redirect(success_url)
        return render(request, "categories/update.html", {"form":form})


