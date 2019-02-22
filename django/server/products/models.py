from django.db import models


class Category(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField(blank = True, null = True,)
    created = models.DateTimeField(auto_now_add = True,)
    modified = models.DateTimeField(auto_now = True,)
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length = 255)
    image = models.ImageField(upload_to = "products", blank = True, null = True,)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, blank = True, null = True,)
    description = models.TextField(blank = True, null = True,)
    cost = models.DecimalField(max_digits = 12, decimal_places = 2, default = 0)
    created = models.DateTimeField(auto_now_add = True,)
    modified = models.DateTimeField(auto_now = True,)
    def __str__(self):
        return self.name
