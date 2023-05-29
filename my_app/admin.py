from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ['picture', 'title']
    # search_fields = ['category__name', 'sub_category__name']
    # list_filter = ['category','subcategory']
    list_per_page = 10


admin.site.register(UsersModel)
admin.site.register(InfoModel)