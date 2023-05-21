# Generated by Django 2.2.8 on 2023-02-08 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_auto_20230130_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='pcr_inspection',
            name='method',
            field=models.CharField(choices=[('Sputum', 'Sputum'), ('기관지내시경 검체', '기관지내시경 검체'), ('기타', '기타')], default='', max_length=20, verbose_name='검사 방법'),
        ),
        migrations.AlterField(
            model_name='sputum_inspection',
            name='method',
            field=models.CharField(choices=[('객담 검체', '객담 검체'), ('기관지경 검체', '기관지경 검체'), ('기타', '기타')], default='', max_length=20, verbose_name='검사 방법'),
        ),
    ]