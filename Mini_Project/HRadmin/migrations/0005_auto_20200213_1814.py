# Generated by Django 3.0.1 on 2020-02-13 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HRadmin', '0004_auto_20200213_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addemployee',
            name='Idno',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]