from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django import forms
from django.utils.html import format_html

class NoDeleteAdminMixin:
    def has_delete_permission(self, request, obj=None):
        #return False # Disable Delete
        return True   # Enable Delete


# ===================================================
# class Article_admin
# ===================================================
class Article_admin(NoDeleteAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'item', 'item_verbose', 'translation')

admin.site.register(Article,Article_admin)
# ===================================================

