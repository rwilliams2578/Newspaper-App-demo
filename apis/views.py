from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views import View

from articles.models import Article, Comment


class ApiArticleListView(LoginRequiredMixin, View):
    """Article List View"""

    def get(self, request, *args, **kwargs):
        """Get Request"""
        article = list(Article.objects.values())
        return JsonResponse(article, safe=False)


class ApiArticleDetailView(LoginRequiredMixin, View):
    """Article Detail View"""

    def get(self, request, article_pk, *args, **kwargs):
        """Get Request"""
        article = Article.objects.values().get(
            pk=article_pk,
        )
        comment = list(
            Comment.objects.filter(
                article_pk=article_pk,
            ).values()
        )
        return JsonResponse(article, safe=False)


class ApiCommentListView(LoginRequiredMixin, View):
    """Comment List View"""

    def get(self, request, article_pk, *args, **kwargs):
        """Get Request"""
        comment = list(
            Comment.objects.filter(
                article_id=article_pk,
            ).values(),
        )
        return JsonResponse(comment, safe=False)


class ApiCommentDetailView(LoginRequiredMixin, View):
    """Comment Detail View"""

    def get(self, request, article_pk, comment_pk, *args, **kwargs):
        comment = Comment.objects.values().get(
            pk=comment_pk,
        )
        return JsonResponse(comment, safe=False)
