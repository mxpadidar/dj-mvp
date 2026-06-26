from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import RedirectView

from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(url="/home")),
    path("home/", views.HomeView.as_view(), name="home"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="login_page.html", extra_context={"title": "Login"}
        ),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
