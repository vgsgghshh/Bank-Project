# Generated by Django 4.2.1 on 2023-07-23 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0010_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='newsid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
