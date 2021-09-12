from django.contrib import admin
from .models import Game, Category, Wishlist, Comment


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


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['wished_item']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'game', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('user', 'game', 'body')
