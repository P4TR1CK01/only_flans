from django.contrib import admin
from main.models import Contact

class PersonaAdmin(admin.ModelAdmin):
  pass

admin.site.register(Contact, PersonaAdmin)