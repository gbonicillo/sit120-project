from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model

User = get_user_model()


class UserAddressInline(admin.StackedInline):
    model = UserAddress


class ShopAddressInline(admin.StackedInline):
    model = ShopAddress


class OrderMenuItemsInline(admin.TabularInline):
    model = Order.menu_items.through


class MenuItemInline(admin.TabularInline):
    model = MenuItem


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [
        UserAddressInline
    ]


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    inlines = [
        ShopAddressInline,
        MenuItemInline
    ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderMenuItemsInline
    ]
    exclude = [
        "menu_items"
    ]
