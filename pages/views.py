from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """Home Page view"""

    template_name = "home.html"
