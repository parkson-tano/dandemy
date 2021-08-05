from django.contrib import admin
from .models import Favorite
# Register your models here.

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_created')

admin.site.register(Favorite, FavoriteAdmin)
