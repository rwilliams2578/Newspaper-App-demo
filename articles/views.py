from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Article


class ArticleListView(ListView):
    """Article List View"""

    model = Article
    template_name = "article_list.html"


class ArticleDetailView(DetailView):
    """Article Detail View"""

    model = Article
    template_name = "article_detail.html"


class ArticleCreateView(CreateView):
    """Article Create View"""

    model = Article
    template_name = "article_new.html"
    fields = ("title", "body", "author")


class ArticleUpdateView(UpdateView):
    """Article Update View"""

    model = Article
    fields = (
        "title",
        "body",
    )
    template_name = "article_edit.html"


class ArticleDeleteView(DeleteView):
    """Article Delete View"""

    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")
