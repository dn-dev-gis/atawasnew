# Generated by Django 3.0.1 on 2020-04-26 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='country',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='email1',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='email2',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='email3',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='email4',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='email5',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='person',
            name='firstnames',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone1',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone2',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone3',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone4',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone5',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone6',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone7',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='person',
            name='pobox',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='person',
            name='position',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='person',
            name='town',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
