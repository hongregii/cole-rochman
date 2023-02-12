# Generated by Django 2.2.8 on 2022-10-07 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20221007_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='vision',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='시력'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='몸무게'),
        ),
    ]
