from django.urls import path
from accounts.views import signup, login, exit

urlpatterns = [
    path("accounts/login/", login, name="login"),
    path("accounts/signup/", signup, name="signup"),
    path("accounts/logout/", exit, name="logout"),
]
