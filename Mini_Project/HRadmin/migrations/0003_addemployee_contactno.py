# Generated by Django 3.0.1 on 2020-02-13 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HRadmin', '0002_addemployee'),
    ]

    operations = [
        migrations.AddField(
            model_name='addemployee',
            name='ContactNO',
            field=models.IntegerField(default=11),
            preserve_default=False,
        ),
    ]
