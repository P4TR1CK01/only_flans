from django.contrib import admin
from main.models import Pizza
# Register your models here.
class PizzaAdmin(admin.ModelAdmin):
  pass

admin.site.register(Pizza, PizzaAdmin)