# Generated by Django 4.2.1 on 2023-06-02 03:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("receipts", "0002_alter_receipt_account"),
    ]

    operations = [
        migrations.AlterField(
            model_name="receipt",
            name="date",
            field=models.DateTimeField(),
        ),
    ]