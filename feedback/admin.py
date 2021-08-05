from django.contrib import admin
from .models import Review
# Create your views here.

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user','course', 'rating', 'date_created')
    list_filter = ('course', 'rating', 'date_created')

admin.site.register(Review, ReviewAdmin)

