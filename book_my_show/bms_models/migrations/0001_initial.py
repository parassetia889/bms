# Generated by Django 4.0.6 on 2022-07-13 07:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('duration_in_min', models.IntegerField(blank=True)),
                ('language', models.CharField(blank=True, max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=64, unique=True)),
                ('phone_number', models.CharField(max_length=32)),
                ('date_of_birth', models.DateField(default=datetime.date.today)),
                ('logged_in_at_utc', models.DateTimeField(default=datetime.datetime.now)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bms_models.city')),
            ],
        ),
        migrations.CreateModel(
            name='Theatre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('number_of_screens', models.IntegerField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bms_models.city')),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_start_time', models.DateTimeField(default=datetime.datetime.now)),
                ('show_end_time', models.DateTimeField(default=datetime.datetime.now)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bms_models.movie')),
                ('screen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bms_models.screen')),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_number', models.CharField(max_length=32)),
                ('screen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bms_models.screen')),
            ],
        ),
        migrations.AddField(
            model_name='screen',
            name='theatre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bms_models.theatre'),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_seats_booked', models.PositiveIntegerField()),
                ('date_of_booking', models.DateField(default=datetime.date.today)),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bms_models.show')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bms_models.user')),
            ],
        ),
        migrations.CreateModel(
            name='BookedSeat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bms_models.booking')),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bms_models.seat')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bms_models.show')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, unique=True)),
                ('password', models.CharField(max_length=64)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bms_models.user')),
            ],
        ),
    ]
