# Generated by Django 4.0.4 on 2022-05-22 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Apps', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuenta',
            name='fechaCompra',
        ),
    ]
