# Generated by Django 4.1.3 on 2022-12-06 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FeeManagement', '0020_alter_monthlyregistration_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlyregistration',
            name='Date',
            field=models.DateField(),
        ),
    ]
