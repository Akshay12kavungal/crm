# Generated by Django 4.1.3 on 2022-12-06 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FeeManagement', '0023_remove_monthlyregistration_invoice1_send'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthlyregistration',
            name='Invoice1_send',
            field=models.CharField(default=0, max_length=42),
        ),
    ]