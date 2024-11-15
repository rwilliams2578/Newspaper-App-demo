from django.conf import settings
from django.db import models
from django.urls import reverse


class Article(models.Model):
    """News Article"""

    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="articles",
    )
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="like_article",
        blank=True,
    )

    def __str__(self):
        """Article as a string"""
        return self.title

    def get_absolute_url(self):
        """Get absolute URL for model"""
        return reverse("article_detail", kwargs={"pk": self.pk})

    def get_like_url(self):
        """Get like url base on pk"""
        return reverse("article_like", kwargs={"pk": self.pk})


class Comment(models.Model):
    """Comment Model"""

    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    text = models.CharField(max_length=140)

    def __str__(self):
        """String method"""
        return self.text

    def get_absolute_url(self):
        """Get the absolute url for the comment"""
        # Would be better to have an actual detail view
        # for the comment and this reverse, but we are
        # just going to take the user to the article list
        # when this is called.
        return reverse("article_list")
