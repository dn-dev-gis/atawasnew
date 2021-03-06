# Generated by Django 3.0.1 on 2020-04-26 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='group',
            field=models.ManyToManyField(to='contacts.Group'),
        ),
        migrations.AlterField(
            model_name='person',
            name='organisation',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.Organisation'),
        ),
    ]
