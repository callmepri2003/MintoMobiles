# Generated by Django 3.2.7 on 2021-10-17 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_auto_20211017_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='login_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('pword', models.CharField(max_length=100)),
            ],
        ),
    ]