from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Flower, Currency


class FlowerAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_img', 'name', 'price', 'currency', 'available',)
    list_display_links = ('name', 'price', 'get_img', 'currency', 'available',)
    search_fields = ('name', 'price',)

    def get_img(self, obj):
        if obj.image:
            return mark_safe(
                f"<div class='div_img_admin'><img style='height: 60px; width: 60px; object-fit: cover;' " +
                f"src='{obj.image.url}' class='img_admin'></div>"
            )
        return "No Image"

    get_img.short_description = 'Image'


admin.site.register(Flower, FlowerAdmin)
admin.site.register(Currency)
