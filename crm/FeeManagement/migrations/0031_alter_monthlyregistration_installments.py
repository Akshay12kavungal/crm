# Generated by Django 4.1.3 on 2022-12-07 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FeeManagement', '0030_alter_monthlyregistration_due_ammount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlyregistration',
            name='Installments',
            field=models.CharField(blank=True, choices=[('First installment', 'First installment'), ('Second installment', 'Second installment'), ('Third installment', 'Third installment')], max_length=42),
        ),
    ]