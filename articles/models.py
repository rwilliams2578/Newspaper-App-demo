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

    def __str__(self):
        """Article as a string"""
        return self.title

    def get_absolute_url(self):
        """Get absolute URL for model"""
        return reverse("article_detail", kwargs={"pk": self.pk})
