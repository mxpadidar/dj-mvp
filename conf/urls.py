from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", RedirectView.as_view(url="/home")),
    path("home/", views.HomeView.as_view(), name="home"),
]
