# Generated by Django 2.2 on 2019-04-25 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_auto_20190417_0140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item',
            new_name='item_name',
        ),
    ]