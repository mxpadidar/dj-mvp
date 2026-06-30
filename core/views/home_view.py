from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home_page.html"
    authentication_required = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "home"
        context["message"] = "welcome to the home page!"
        return context
