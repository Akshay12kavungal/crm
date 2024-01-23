# Generated by Django 4.1.3 on 2022-12-06 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FeeManagement', '0006_alter_monthlyregistration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlyregistration',
            name='Due_Ammount_Date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='monthlyregistration',
            name='Paymement_Mode',
            field=models.CharField(choices=[('CASH', 'CASH'), ('UPI', 'UPI'), ('NFET', 'NFET')], max_length=42),
        ),
        migrations.AlterField(
            model_name='monthlyregistration',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Nil', 'Nil')], max_length=42),
        ),
    ]
