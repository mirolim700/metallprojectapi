from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

@admin.register(ProductsModel)
class ProductAdmin(TranslationAdmin):
    list_display = ['picture', 'title']
    list_per_page = 10

# admin.site.register(ProductsModel)

admin.site.register(InfoModel)

admin.site.register(UsersModel)
