from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse

from .forms import CommentForm

from .models import Article


class ArticleListView(LoginRequiredMixin, ListView):
    """Article List View"""

    model = Article
    template_name = "article_list.html"


class ArticleDetailView(LoginRequiredMixin, DetailView, FormView):
    """Article Detail View"""

    model = Article
    form_class = CommentForm
    template_name = "article_detail.html"

    def post(self, request, *args, **kwargs):
        """Handle post request"""
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        article = self.object
        return reverse("article_detail", kwargs={"pk": article.pk})


class ArticleCreateView(LoginRequiredMixin, CreateView):
    """Article Create View"""

    model = Article
    template_name = "article_new.html"
    fields = ("title", "body")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Article Update View"""

    model = Article
    fields = (
        "title",
        "body",
    )
    template_name = "article_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Article Delete View"""

    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleLikeView(LoginRequiredMixin, View):
    """Article Like View"""

    def get(self, request, *args, **kwargs):
        """Get Request"""
        # Get out the data from the Get request
        article_id = request.GET.get("article_id", None)
        article_action = request.GET.get("article_action", None)

        if not article_id or not article_action:
            return JsonResponse(
                {
                    "success": False,
                }
            )

        article = Article.objects.get(id=article_id)
        if article_action == "like":
            # Do like stuff
            article.likes.add(request.user)
        else:
            # Do unlike stuff
            article.likes.remove(request.user)

        return JsonResponse(
            {
                "success": True,
            }
        )
