from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(url="/home")),
    path("home/", views.HomeView.as_view(), name="home"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="login_page.html",
            next_page=reverse_lazy("profile"),
            redirect_authenticated_user=True,
            extra_context={"title": "Login"},
        ),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(
            next_page=reverse_lazy("login"),
        ),
        name="logout",
    ),
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("profile/update/", views.ProfileUpdateView.as_view(), name="profile-update"),
    path(
        "password/change/",
        auth_views.PasswordChangeView.as_view(
            template_name="password_change_page.html",
            success_url=reverse_lazy("password-change-done"),
            extra_context={"title": "Change Password"},
        ),
        name="password-change",
    ),
    path(
        "password/change/done/",
        auth_views.PasswordChangeDoneView.as_view(
            template_name="password_change_done_page.html",
            extra_context={"title": "Password Changed"},
        ),
        name="password-change-done",
    ),
]
