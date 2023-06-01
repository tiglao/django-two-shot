from django.urls import path
from receipts.views import receipts

urlpatterns = [
    path("", receipts, name="home"),
]

if urlpatterns:
    print("urlpatterns can be found")
