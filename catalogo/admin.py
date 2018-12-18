from django.contrib import admin

from .models import Product, Category


class CategoriaAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'created', 'modified']
    search_fields = ['name']
    list_filter = ['created', 'modified']


class ProdutoAmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'created', 'modified']
    search_fields = ['name', 'slug', 'category__name']
    list_filter = ['created', 'modified']


admin.site.register(Category, CategoriaAdmin)
admin.site.register(Product, ProdutoAmin)
