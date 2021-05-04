from django.contrib import admin

from recipe import models


class RecipeAdmin(admin.ModelAdmin):
    ordering = ['title']
    search_fields = ['title']
    list_display = ['title', 'time_minutes', 'price']


admin.site.register(models.Ingredient)
admin.site.register(models.Recipe, RecipeAdmin)
