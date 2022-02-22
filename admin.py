from django.contrib import admin
from . models import Customer,Product,Employee,Office,Movie,Song

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Employee)
admin.site.register(Office)
admin.site.register(Movie)
admin.site.register(Song)