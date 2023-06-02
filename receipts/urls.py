from django.urls import path
from receipts.views import (
    receipt_list,
    create_receipt,
    category_table,
    account_table,
    create_category,
)

urlpatterns = [
    path("", receipt_list, name="home"),
    path("create/", create_receipt, name="create_receipt"),
    path("categories/create/", create_category, name="create_category"),
    path("categories/", category_table, name="category_list"),
    path("accounts/", account_table, name="account_list"),
]
