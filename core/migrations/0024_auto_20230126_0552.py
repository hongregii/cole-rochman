# Generated by Django 2.2.8 on 2023-01-26 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_post_print_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='pcr_inspection',
            name='pcr_date',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='sputum_inspection',
            name='sputum_date',
            field=models.CharField(default='', max_length=20),
        ),
    ]