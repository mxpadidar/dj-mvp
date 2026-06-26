from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import View

from core.forms import ProfileUpdateForm


class ProfileUpdateView(LoginRequiredMixin, View):
    template_name = "profile_update_page.html"

    def get(self, request):
        form = ProfileUpdateForm(instance=request.user)
        return render(
            request,
            self.template_name,
            {"form": form, "title": "Edit Profile"},
        )

    def post(self, request):
        form = ProfileUpdateForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect("profile")

        return render(request, self.template_name, {"form": form})
