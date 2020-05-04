# Generated by Django 3.0.1 on 2020-04-27 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20200427_1112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='articles/images/')),
                ('issue', models.IntegerField()),
                ('year', models.IntegerField()),
                ('file', models.ImageField(upload_to='articles/images/')),
            ],
        ),
    ]