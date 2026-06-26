from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from core.models import User


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile_page.html"

    def get_context_data(self, **kwargs):
        user: User = self.request.user  # type: ignore

        context = super().get_context_data(**kwargs)
        context["title"] = "Profile"
        context["profile"] = [
            ("username", user.username),
            ("email", user.email or "-"),
            ("first name", user.first_name or "-"),
            ("last name", user.last_name or "-"),
            (
                "last login",
                user.last_login.strftime("%y-%m-%d %h:%m")
                if user.last_login
                else "never",
            ),
            ("date joined", user.date_joined.strftime("%y-%m-%d %h:%m")),
        ]
        return context
