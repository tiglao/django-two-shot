from django.urls import path
from receipts.views import receipts


urlpatterns = [
    path("", receipts, name="home"),
]
