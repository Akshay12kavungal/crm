# Generated by Django 4.1.3 on 2022-12-06 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FeeManagement', '0014_alter_monthlyregistration_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlyregistration',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Payment completed', 'Payment completed')], max_length=42),
        ),
    ]