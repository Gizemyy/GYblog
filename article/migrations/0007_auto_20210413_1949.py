# Generated by Django 3.1.7 on 2021-04-13 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_auther',
            new_name='comment_author',
        ),
    ]