# Generated by Django 4.1.7 on 2023-04-08 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blogApp", "0004_comment_recomment"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="post",
            new_name="article",
        ),
    ]
