from django.contrib import admin
from .models import *
# Register your models here.

class CartItemInline(admin.TabularInline):
    model=CartItem
    extra=0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','brand','inventory','price','category')
    list_filter=('brand','category')
    fields=('name',('brand','category'),('price','inventory'),'description')
    inlines=[CartItemInline]

class CartItemAdmin(admin.ModelAdmin):
    list_display=('product','user','quantity')

class UserAdmin(admin.ModelAdmin):
    list_display=('username','email','first_name')
    inlines=[CartItemInline]
admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(CartItem,CartItemAdmin)