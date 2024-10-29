from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Articles


class ArticleListView(ListView):
    """Article List View"""

    model = Articles
    template_name = "article_list.html"


class ArticleDetailView(DetailView):
    """Article Detail View"""

    model = Articles
    template_name = "article_detail.html"


class ArticleUpdateView(UpdateView):
    """Article Update View"""

    model = Articles
    fields = (
        "title",
        "body",
    )
    template_name = "article_edit.html"


class ArticleDeleteView(DeleteView):
    """Article Delete View"""

    model = Articles
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")
