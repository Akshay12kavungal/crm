# Generated by Django 4.1.3 on 2022-12-06 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FeeManagement', '0012_alter_monthlytransaction_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlytransaction',
            name='City',
            field=models.CharField(choices=[('Bangalore', 'Bangalore'), ('Pune', 'Pune'), ('Other', 'Other')], max_length=42),
        ),
        migrations.AlterField(
            model_name='monthlytransaction',
            name='Payed_to_account',
            field=models.CharField(choices=[('Bangalore', 'Bangalore'), ('Pune', 'Pune'), ('Other', 'Other')], max_length=42),
        ),
    ]
