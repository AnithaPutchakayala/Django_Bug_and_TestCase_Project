# Generated by Django 3.2.5 on 2021-11-01 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcase',
            name='date_of_creation',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]