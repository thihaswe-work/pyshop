from django.contrib import admin
from .models import Cart, CartItem, Order


class CartItemInline(admin.TabularInline):
    model = CartItem


class CartAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "session_key", "created_at")
    inlines = [CartItemInline]


class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "full_name", "total", "status", "created_at")
    list_filter = ("status",)
    search_fields = ("full_name", "email")


admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)
