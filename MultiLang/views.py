from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext
from .models import *

# ===================================================
# Home page function to translate items as per current 
# application language and and send back to index.html page
# ===================================================
def home(request):
    data = {
        'header': translate(item = 'header'),
        'wid1_title': translate(item = 'wid1_title'),
        'wid1_body': translate(item = 'wid1_body'),
        'wid1_btn_text': translate(item = 'wid1_btn_text'),
        'wid2_title': translate(item = 'wid2_title'),
        'wid2_body': translate(item = 'wid2_body'),
        'wid2_btn_text': translate(item = 'wid2_btn_text'),
        'wid3_title': translate(item = 'wid3_title'),
        'wid3_body': translate(item = 'wid3_body'),
        'wid3_btn_text': translate(item = 'wid3_btn_text'),
    }

    return render(request, 'index.html', data)
# ===================================================



# ===================================================
# Function translate item text by querying on model
# ===================================================
def translate(item):
    cur_language = get_language()
    try:
        trans_dict_name = 'translation__' + cur_language
        text = Article.objects.filter(item = item).values(trans_dict_name)

        if len(text) > 0:
            text = text[0][trans_dict_name]
        else:
            text = ''

    finally:
        activate(cur_language)
    return text

# ===================================================