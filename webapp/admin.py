from django.contrib import admin
from pyrsistent import v
from .models import employees

list_display=['picture']
admin.site.register(employees)

# Register your models here.


