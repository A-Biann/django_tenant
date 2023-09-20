from django.contrib import admin
from products.models import Product, ProductCategory, ProductImage

class ProductImageInline(admin.TabularInline): # 內嵌管理介面
    model = ProductImage
    fields = ('name', 'image', 'order')

class ProductAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'price', 'category', 'created', 'modified')
    list_display = ('name', 'price', 'category',)
    list_filter = ('category',)
    autocomplete_fields = ['category']
    readonly_fields = ('created', 'modified')
    inlines = [ProductImageInline, ]
    
class ProductCategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'created', 'modified', 'image')
    list_display = ('name',)
    search_fields = ['name']
    readonly_fields = ('created', 'modified')

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)