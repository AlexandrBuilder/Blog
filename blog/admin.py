from django.contrib import admin

from .models import Post, Comment, Like, Property


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'annotation')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('body', 'author', 'post', 'created', 'active')
    list_filter = ('active', 'created')
    search_fields = ('body', 'body')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('author', 'post')


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('title',)