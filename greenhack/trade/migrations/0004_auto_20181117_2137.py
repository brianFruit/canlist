# Generated by Django 2.1.2 on 2018-11-17 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0003_auto_20181117_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cbd',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='thc',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
    ]
