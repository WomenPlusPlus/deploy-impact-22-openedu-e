from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Resource

# Register your models here.

admin.site.register(Resource, TranslatableAdmin)
