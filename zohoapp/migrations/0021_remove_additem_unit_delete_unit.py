# Generated by Django 4.1 on 2023-06-12 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0020_rename_user_id_unit_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='additem',
            name='unit',
        ),
        migrations.DeleteModel(
            name='Unit',
        ),
    ]
