from modeltranslation.translator import TranslationOptions, translator

from .models import Banner, Product


# for Person model
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

translator.register(Product, ProductTranslationOptions)

class BannerTranslationOptions(TranslationOptions):
    fields = ('title', 'summary', 'body')

translator.register(Banner, BannerTranslationOptions)