# Generated by Django 3.0.1 on 2020-04-27 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_delete_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('website', models.URLField(max_length=150)),
                ('pobox', models.CharField(max_length=150)),
                ('town', models.CharField(max_length=150)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.MemberType')),
            ],
        ),
    ]
