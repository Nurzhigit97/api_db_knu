from django.contrib import admin
from db.models import *
# Register your models here.
class GlossaryAdmin(admin.ModelAdmin):
    list_display =  [field.name for field in Glossary._meta.fields]


admin.site.register (Glossary, GlossaryAdmin)