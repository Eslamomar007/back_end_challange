from django.contrib import admin
from coffee.models import Product, Pods, Machines
# Register your models here.
admin.site.register(Product)
admin.site.register(Pods)
admin.site.register(Machines)
