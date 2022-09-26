from django.contrib import admin
from .models import Product, Brand


# Register your models here.
class ProductInline(admin.TabularInline):
    model = Product
    extra = 3


class BrandAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Basic information", {'fields': ['name']}),
    ]
    inlines = [ProductInline]


admin.site.register(Brand, BrandAdmin)
admin.site.register(Product)