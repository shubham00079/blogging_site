# Generated by Django 3.0.7 on 2020-07-15 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_published_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_on',
            new_name='created_date',
        ),
    ]
