from django.contrib import admin
from .models import Name,Image,tags

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

# Register your models here.
admin.site.register(Name)
admin.site.register(Image)
admin.site.register(tags)
