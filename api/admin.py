from django.contrib import admin
from .models import Vote, Color, User


class ColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'hexa')


admin.site.register(Vote)
admin.site.register(User)
admin.site.register(Color, ColorAdmin)
