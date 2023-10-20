# myapp/admin.py
from django.contrib import admin
from .models import MyModel

class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(MyModel, MyModelAdmin)
