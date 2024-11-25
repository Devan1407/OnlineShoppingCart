from django.contrib import admin

# Register your models here.
from . models import Category,Product

class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields = {'slug':['name',]}
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','stock','available','updated  ','created']
    list_editable = ['price','available','stock']
    prepopulated_fields = {'slug':['name',]}
admin.site.register(Product,ProductAdmin)

