# Generated by Django 3.2.4 on 2021-07-08 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Blog', '0002_auto_20210707_1841'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-publish_date']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-comment_date',)},
        ),
    ]
