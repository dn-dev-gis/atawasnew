# Generated by Django 3.0.1 on 2020-04-27 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_members_membertype'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Members',
            new_name='Member',
        ),
    ]