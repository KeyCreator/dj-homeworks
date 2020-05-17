from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
    ordering = ('-id', )
    list_display = ('brand', 'model', 'review_count')
    search_fields = ('brand', 'model', )
    list_filter = ('brand', 'model', )


class ReviewAdmin(admin.ModelAdmin):
    ordering = ('-id', )
    list_display = ('car', 'title', )
    search_fields = ('car', 'title', )
    list_filter = ('car', 'title', )

    form = ReviewAdminForm


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
