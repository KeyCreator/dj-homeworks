from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path
from .views import table_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('table/', table_view),
    path('', lambda x: HttpResponseRedirect('/table/')),
]