# Generated by Django 4.0.6 on 2023-11-02 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Railway',
            fields=[
                ('Railway_id', models.AutoField(primary_key=True, serialize=False)),
                ('Railway_name', models.CharField(max_length=255)),
                ('Railway_website', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RailwaySystem',
            fields=[
                ('RailwaySystem_id', models.AutoField(primary_key=True, serialize=False)),
                ('RailwaySystem_name', models.CharField(max_length=255)),
                ('RailwaySystem_address', models.CharField(max_length=255)),
                ('RailwaySystem_phone_number', models.CharField(max_length=255)),
                ('RailwaySystem_website', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('train_id', models.AutoField(primary_key=True, serialize=False)),
                ('train_number', models.CharField(max_length=255)),
                ('departure_date', models.DateField()),
                ('arrival_date', models.DateField()),
                ('departure_time', models.TimeField()),
                ('arrival_time', models.TimeField()),
                ('train_status', models.CharField(max_length=255)),
                ('Railway', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FE_Railway.railway')),
                ('arrival_RailwaySystem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrivals', to='FE_Railway.railwaysystem')),
                ('departure_RailwaySystem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departures', to='FE_Railway.railwaysystem')),
            ],
        ),
    ]
