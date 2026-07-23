from django.contrib import admin
from .models import Product, Offer, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "stock")
    list_filter = ("category",)
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


class OfferAdmin(admin.ModelAdmin):
    list_display = ("code", "description", "discount")


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name",)


admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Category, CategoryAdmin)
