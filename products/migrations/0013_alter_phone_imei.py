# Generated by Django 3.2.7 on 2021-09-17 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_phone_imei'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='IMEI',
            field=models.CharField(default='00', max_length=200),
        ),
    ]
