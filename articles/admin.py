from django.contrib import admin
from .models import Article, Comment


class CommentInline(admin.StackedInline):
    """Comment Inline for Article Admin"""

    # Could use admin.StackedInline as the class to
    # inherit from if we wanted a different looking
    # inline that is "stacked" vs "horizontal"

    model = Comment


class ArticleAdmin(admin.ModelAdmin):

    inlines = [CommentInline]


# Register your models here
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
