# Generated by Django 3.1.6 on 2021-06-13 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0015_auto_20210610_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='mapImage',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]