# Generated by Django 2.0.7 on 2018-09-25 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaignapp', '0004_auto_20180924_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='interest_type',
            field=models.IntegerField(choices=[(1, 'BUNDLE'), (2, 'PRECISE')]),
        ),
    ]
