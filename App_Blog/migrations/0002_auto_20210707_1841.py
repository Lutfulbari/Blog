# Generated by Django 3.2.4 on 2021-07-07 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='bolg_image',
            new_name='blog_image',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='bolg_title',
            new_name='blog_title',
        ),
    ]
