# Generated by Django 2.1.1 on 2018-09-13 13:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ballots', '0006_auto_20180913_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='party_date_registered',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='party date registered'),
        ),
    ]