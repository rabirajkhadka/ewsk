# Generated by Django 3.1.6 on 2021-02-24 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_auto_20210223_1335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drainagetrend',
            name='trendID',
        ),
        migrations.AddField(
            model_name='drainagetrend',
            name='id',
            field=models.AutoField(
                auto_created=True,  primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]