# Generated by Django 4.1 on 2023-06-15 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0026_alter_additem_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurring_bills',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='doc/recurring_bills'),
        ),
        migrations.AlterField(
            model_name='recurring_bills',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recurring_bills',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
