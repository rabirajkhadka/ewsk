# Generated by Django 3.1.6 on 2021-06-13 16:33

from django.db import migrations, models
import webapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0017_auto_20210613_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='mapImage',
            field=models.ImageField(blank=True, null=True, upload_to=webapp.models.upload_location),
        ),
    ]
