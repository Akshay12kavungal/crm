# Generated by Django 4.1.3 on 2022-12-06 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FeeManagement', '0026_alter_monthlyregistration_ammount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlytransaction',
            name='PaymentMode',
            field=models.CharField(choices=[('CASH', 'CASH'), ('UPI', 'UPI'), ('NFET', 'NFET')], max_length=42),
        ),
    ]
