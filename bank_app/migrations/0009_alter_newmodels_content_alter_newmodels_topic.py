# Generated by Django 4.2.1 on 2023-07-19 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0008_rename_newmodel_newmodels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newmodels',
            name='content',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='newmodels',
            name='topic',
            field=models.CharField(max_length=500),
        ),
    ]
