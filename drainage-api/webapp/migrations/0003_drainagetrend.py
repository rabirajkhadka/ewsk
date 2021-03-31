# Generated by Django 3.1.6 on 2021-02-23 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_delete_drainagetrend'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrainageTrend',
            fields=[
                ('trendID', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('trendValue', models.DecimalField(decimal_places=3, max_digits=10)),
                ('dateTime', models.DateTimeField()),
                ('station', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='webapp.station')),
            ],
        ),
    ]