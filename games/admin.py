from django.contrib import admin
from .models import Game, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'year', 'created']
    list_filter = ['year', 'created']
    # list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('title',)}
