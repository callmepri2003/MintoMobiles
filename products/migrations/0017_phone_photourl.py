# Generated by Django 3.2.7 on 2021-09-17 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_phone_imei'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='photoURL',
            field=models.CharField(default="{% static '<django.db.models.fields.related.ForeignKey>/<django.db.models.fields.related.ForeignKey>' %}", max_length=20),
        ),
    ]