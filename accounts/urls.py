from django.urls import path
from accounts.views import signup, exit

urlpatterns = [
    path("accounts/login/", signup, name="login"),
    path("logout/", exit, name="logout"),
]
