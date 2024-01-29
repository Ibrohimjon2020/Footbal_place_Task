from modeltranslation.translator import TranslationOptions, translator

from .models import Category


# for Person model
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'title', 'head_name', 'hashtag_name')

translator.register(Category, CategoryTranslationOptions)
