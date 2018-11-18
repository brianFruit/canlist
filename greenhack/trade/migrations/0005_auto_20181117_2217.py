# Generated by Django 2.1.2 on 2018-11-17 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0004_auto_20181117_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='posting',
            name='lat',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='posting',
            name='lon',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='posting',
            name='wishlist',
            field=models.TextField(null=True),
        ),
    ]
