from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


def redirect_home(request):
    return redirect("home")


urlpatterns = [
    path("", include("receipts.urls")),
    path("", include("accounts.urls")),
    path("", redirect_home),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
]
