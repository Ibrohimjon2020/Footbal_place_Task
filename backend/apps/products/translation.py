from modeltranslation.translator import translator, TranslationOptions
from .models import Product, Banner

# for Person model
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

translator.register(Product, ProductTranslationOptions)

class BannerTranslationOptions(TranslationOptions):
    fields = ('title', 'summary', 'body')

translator.register(Banner, BannerTranslationOptions)