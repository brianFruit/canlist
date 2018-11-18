# Generated by Django 2.1.2 on 2018-11-17 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0005_auto_20181117_2217'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posting',
            old_name='qantity',
            new_name='quantity',
        ),
        migrations.AlterField(
            model_name='posting',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
    ]
