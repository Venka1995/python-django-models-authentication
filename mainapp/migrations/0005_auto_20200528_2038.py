# Generated by Django 3.0.4 on 2020-05-28 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_blogpost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='auther',
            new_name='author',
        ),
    ]
