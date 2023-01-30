from django.db import models


class Article(models.Model):
    item = models.CharField(max_length = 255, default=None, unique=True, verbose_name="Item Name")
    item_verbose = models.CharField(max_length = 255, null=True, default=None, verbose_name="Item Verbose Name")
    translation = models.JSONField(null=True, blank=True, default=dict, verbose_name="Translation")
    
    class Meta:
        managed = True
        db_table = 'article'
        verbose_name="Article"
        verbose_name_plural="Article"
    def __str__(self):
        return str(self.id)


