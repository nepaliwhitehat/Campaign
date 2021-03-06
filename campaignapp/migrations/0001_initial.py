# Generated by Django 2.0.7 on 2018-09-21 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('date_deleted', models.DateField(blank=True, null=True)),
                ('name', models.CharField(max_length=120)),
                ('url', models.CharField(max_length=120)),
                ('min_age', models.IntegerField()),
                ('max_age', models.IntegerField()),
                ('gender', models.IntegerField(choices=[('MALE', 1), ('FEMALE', 2)])),
                ('address_type', models.IntegerField(choices=[('COUNTRY', 1), ('STATE', 2), ('CITY', 3)])),
                ('address', models.CharField(max_length=120, null=True)),
                ('any_address', models.CharField(blank=True, max_length=120, null=True)),
                ('devices', models.IntegerField(choices=[('MOBILE', 1), ('DESKTOP', 2)])),
                ('interest_type', models.IntegerField(choices=[('BUNDLE', 1), ('PRECISE', 2)])),
                ('price', models.FloatField()),
                ('daily_visitors', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InterestBundle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('date_deleted', models.DateField(blank=True, null=True)),
                ('name', models.CharField(max_length=120)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='campaign',
            name='interest_bundle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='campaignapp.InterestBundle'),
        ),
    ]
