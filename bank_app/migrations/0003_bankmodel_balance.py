# Generated by Django 4.2.1 on 2023-07-03 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0002_rename_image_bankmodel_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankmodel',
            name='balance',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
