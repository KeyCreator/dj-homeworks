from django.contrib import admin
from phones.models import Phone, Feature

# Register your models here.
@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    pass


class FeatureAdmin(admin.ModelAdmin):
    pass


admin.site.register(Feature, FeatureAdmin)