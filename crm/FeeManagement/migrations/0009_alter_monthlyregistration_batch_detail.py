# Generated by Django 4.1.3 on 2022-12-06 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FeeManagement', '0008_alter_monthlyregistration_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlyregistration',
            name='Batch_Detail',
            field=models.CharField(choices=[('WEEKDAY ONLINE SESSION', 'WEEKDAY ONLINE SESSION'), ('WEEKDAY OFFLINE SESSION', 'WEEKDAY OFFLINE SESSION'), ('WEEKEND ONLINE SESSION', 'WEEKEND ONLINE SESSION'), ('WEEKEND OFFLINE SESSION', 'WEEKEND OFFLINE SESSION')], max_length=42),
        ),
    ]
