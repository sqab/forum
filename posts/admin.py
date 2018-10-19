from django.contrib import admin
from .models import Post, CommentPost, Like, Hit


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'created_date')


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'text', 'created')


admin.site.register(CommentPost, CommentAdmin)


class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'created')


admin.site.register(Like, LikeAdmin)


class HitAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'created')


admin.site.register(Hit, HitAdmin)
