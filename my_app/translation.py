from .models import ProductsModel
from modeltranslation.translator import register, TranslationOptions

@register(ProductsModel)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title',)