from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from receipts.models import Receipt, ExpenseCategory, Account
from receipts.forms import ReceiptForm, CategoryForm, AccountForm


@login_required
def receipt_list(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context = {"receipts": receipts}
    return render(request, "receipts/list.html", context)


@login_required
def create_receipt(request):
    if request.method == "POST":
        form = ReceiptForm(user=request.user, data=request.POST)
        if form.is_valid():
            receipt = form.save(False)
            receipt.purchaser = request.user
            receipt.category = form.cleaned_data["category_table"]
            receipt.account = form.cleaned_data["account_table"]
            receipt.save()
            return redirect("home")
    else:
        form = ReceiptForm(user=request.user)

    context = {
        "form": form,
    }

    return render(request, "receipts/create.html", context)


@login_required
def category_table(request):
    categories = ExpenseCategory.objects.filter(owner=request.user)

    context = {"category_table": categories}

    return render(request, "receipts/list_categories.html", context)


@login_required
def account_table(request):
    accounts = Account.objects.filter(owner=request.user)

    context = {"account_table": accounts}

    return render(request, "receipts/list_accounts.html", context)


@login_required
def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(False)
            category.owner = request.user
            category.save()
            return redirect("category_list")
    else:
        form = CategoryForm()

    context = {
        "form": form,
    }

    return render(request, "receipts/create_category.html", context)


@login_required
def create_account(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(False)
            account.owner = request.user
            account.save()
            return redirect("account_list")
    else:
        form = AccountForm()

    context = {
        "form": form,
    }

    return render(request, "receipts/create_account.html", context)
