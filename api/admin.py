from django.contrib import admin
from .models import Vote, Color


admin.site.register([Vote, Color])
