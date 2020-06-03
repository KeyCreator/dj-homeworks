from django.contrib import admin
from .models import TableField, FilePath


# Register your models here.
@admin.register(TableField)
class TableFieldAdmin(admin.ModelAdmin):
    pass


@admin.register(FilePath)
class FilePathAdmin(admin.ModelAdmin):
    pass

