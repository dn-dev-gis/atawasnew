# Generated by Django 3.0.1 on 2020-04-26 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_person'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]