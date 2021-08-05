from django.contrib import admin
from .models import Cart, CartCourse
# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ('user','total','date_created')
    list_filter = ('total','date_created')

class CartCourseAdmin(admin.ModelAdmin):
    list_display = ('cart','subtotal','date_created')
    list_filter = ('subtotal','date_created')

admin.site.register(CartCourse, CartCourseAdmin)
admin.site.register(Cart, CartAdmin)
