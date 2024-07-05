from django.contrib import admin
from blog.models import Post, Tag, Comment



admin.site.register(Tag)


@admin.register(Comment)
class CommentAdminPanel(admin.ModelAdmin):
    list_display = ['author', 'text', 'post']
    raw_id_fields = ['author']


@admin.register(Post)
class PostAdminPanel(admin.ModelAdmin):
    raw_id_fields = ['author', 'likes', 'tags']
