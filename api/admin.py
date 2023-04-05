from django.contrib import admin
from .models import Vote, Color

# Register your models here.
admin.site.register([Vote, Color])
