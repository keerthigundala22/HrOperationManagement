# Generated by Django 2.1 on 2020-03-06 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicant', '0003_auto_20200306_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicantregistration',
            name='Gender1',
            field=models.BooleanField(default=False, verbose_name='Female'),
        ),
        migrations.AlterField(
            model_name='applicantregistration',
            name='Gender',
            field=models.BooleanField(default=False, verbose_name='Male'),
        ),
    ]
