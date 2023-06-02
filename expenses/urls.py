from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


def redirect_to_receipts(request):
    return redirect("home")


urlpatterns = [
    path("receipts/", include("receipts.urls")),
    path("", include("accounts.urls")),
    path("", redirect_to_receipts),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
]
