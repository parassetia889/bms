from django.db import models
from datetime import date, datetime

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=64)


class User(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=64, unique=True)
    phone_number = models.CharField(max_length=32)
    date_of_birth = models.DateField(default=date.today)
    logged_in_at_utc = models.DateTimeField(default=datetime.now)
    city = models.ForeignKey(City, on_delete=models.CASCADE)


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=64)


class Theatre(models.Model):
    name = models.CharField(max_length=64)
    number_of_screens = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)


class Screen(models.Model):
    screen_number = models.IntegerField()
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)


class Seat(models.Model):
    seat_number = models.CharField(max_length=32)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)


class Movie(models.Model):
    name = models.CharField(max_length=64)
    duration_in_min = models.IntegerField(blank=True)
    language = models.CharField(max_length=32, blank=True)


class Show(models.Model):
    show_start_time = models.DateTimeField(default=datetime.now)
    show_end_time = models.DateTimeField(default=datetime.now)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    number_of_seats_booked = models.PositiveIntegerField()
    date_of_booking = models.DateField(default=date.today)


class BookedSeat(models.Model):
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
