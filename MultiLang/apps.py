from django.apps import AppConfig
from core.settings import *

class MultilangConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "MultiLang"

    def ready(self):
        # ===================================================
        '''
            When Django’s LANGUAGES parameter is updated 
            (e.g. one more language is added/removed), a 
            corresponding field must be added/removed automatically
        '''
        from .models import Article
        try:
            item_data = Article.objects.all().values()  # Get all Article model data
            
            settings_lang = [lang[0] for lang in LANGUAGES] # Getting all available language code from settings.py file
            
            for lang_dict in item_data:

                # Add new language code to JSONfield of all items if it not present in the translation JSONfield data
                for lang in settings_lang:
                    if lang not in lang_dict['translation'].keys():
                        lang_dict['translation'][lang] = ''

                # ===================================================
                ''' 
                    Get language codes of the translation JSONfield data, 
                    which are not present in the available language codes 
                    of the application and delete them from the translation 
                    JSONfield data
                '''
                unique_key = [item for item in lang_dict['translation'].keys() if item not in settings_lang]
                for del_lang in unique_key:
                    del lang_dict['translation'][del_lang]
                # ===================================================

                Article.objects.filter(id=lang_dict['id']).update(translation=lang_dict['translation']) # Update Article model objects

        except:
            print("Table migration required")
        # ===================================================

