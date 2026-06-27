from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views import View

from core.forms import SignupForm


class SignupView(View):
    template_name = "signup_page.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("profile")

        return render(
            request,
            self.template_name,
            {
                "title": "Sign Up",
                "form": SignupForm(),
            },
        )

    def post(self, request):
        if request.user.is_authenticated:
            return redirect("profile")

        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile")

        return render(
            request,
            self.template_name,
            {
                "form": form,
            },
        )
