from django.contrib import admin

from .models import Article, Genre, Author


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('author', 'genre', 'title', 'text', 'published_at', 'image',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone',)
