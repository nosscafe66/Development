from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import (
  Create
  ,Category
  ,Home
  ,Portfolio
  ,Contact
  ,Myart
  ,Logoart
  ,Videoart
  ,Webdesign
)


admin.site.register(Create)
admin.site.register(Category)
admin.site.register(Home)
admin.site.register(Contact)


class ArtImage(admin.ModelAdmin):
    def icon_image(self, obj):
        return mark_safe('<img src="{}" style="width:100px;height:auto;">'.format(obj.image.url))

    list_display = ('project_name', 'image')


admin.site.register(Portfolio, ArtImage)
admin.site.register(Myart, ArtImage)
admin.site.register(Logoart, ArtImage)
admin.site.register(Videoart, ArtImage)
admin.site.register(Webdesign, ArtImage)