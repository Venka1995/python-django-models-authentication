# Generated by Django 3.0.4 on 2020-05-27 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20191004_0501'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogPost',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]