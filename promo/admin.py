from django.contrib import admin
from promo.models import Category, Promotion, Recom, Slides, Pre_order, Registers, Cart, CartItem, Product, Order, OrderItem, OrderPartner

class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','stock','created','updated']
    list_editable=['price','stock']
    list_per_page=10

class OrderAdmin(admin.ModelAdmin):
    list_display=['id','name','email','total','token','created','updated']
    list_per_page=10

class OrderItemAdmin(admin.ModelAdmin):
    list_display=['order','product','quantity','price','created','updated']
    list_per_page=10

class OrderPartnerAdmin(admin.ModelAdmin):
    list_display=['orderId','username','email','created','updated']
    list_per_page=10

# Register your models here.

admin.site.register(Category)
admin.site.register(Promotion)
admin.site.register(Recom)
admin.site.register(Slides)
# admin.site.register(Pre_order)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem,OrderItemAdmin)
admin.site.register(OrderPartner,OrderPartnerAdmin)
admin.site.register(Registers)