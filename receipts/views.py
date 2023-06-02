from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from receipts.models import Receipt, ExpenseCategory, Account
from receipts.forms import ReceiptForm


@login_required
def receipt_list(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context = {"receipts": receipts}
    return render(request, "receipts/list.html", context)


@login_required
def create_receipt(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(False)
            receipt.purchaser = request.user
            receipt.save()
            return redirect("home")
    else:
        form = ReceiptForm()

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
