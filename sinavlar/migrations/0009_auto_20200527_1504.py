# Generated by Django 3.0.5 on 2020-05-27 15:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sinavlar', '0008_auto_20200527_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='testler',
            name='test_sayi',
            field=models.PositiveSmallIntegerField(default='0'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='konular',
            name='konular_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 27, 15, 4, 19, 218614, tzinfo=utc), verbose_name='Yayınlandığı tarih'),
        ),
        migrations.AlterField(
            model_name='testler',
            name='test_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 27, 15, 4, 19, 219366, tzinfo=utc), verbose_name='Yayınlandığı tarih'),
        ),
    ]
