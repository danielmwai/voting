# Generated by Django 2.1.1 on 2018-09-13 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ballots', '0004_auto_20180913_1057'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='candidate',
            options={'ordering': ('date_registered',)},
        ),
        migrations.AlterModelOptions(
            name='party',
            options={'ordering': ('party_name',)},
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='party',
        ),
        migrations.AddField(
            model_name='party',
            name='candidate',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ballots.Candidate'),
        ),
    ]
