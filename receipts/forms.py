from django.forms import ModelForm, ModelChoiceField
from receipts.models import Receipt, ExpenseCategory, Account


class ReceiptForm(ModelForm):
    category_table = ModelChoiceField(queryset=ExpenseCategory.objects.none())
    account_table = ModelChoiceField(queryset=Account.objects.none())

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super(ReceiptForm, self).__init__(*args, **kwargs)
        if user is not None:
            self.fields[
                "category_table"
            ].queryset = ExpenseCategory.objects.filter(owner=user)
            self.fields["account_table"].queryset = Account.objects.filter(
                owner=user
            )

    class Meta:
        model = Receipt
        fields = (
            "vendor",
            "total",
            "tax",
            "date",
            "category_table",
            "account_table",
        )


class CategoryForm(ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = ("name",)


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = (
            "name",
            "number",
        )
