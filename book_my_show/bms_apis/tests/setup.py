from bms_models.models import City, Movie, Screen, Show, Theatre
from django.contrib.auth.models import User
from django.utils import timezone


class SetUp:

    def setup():
        Movie.objects.create(name='Bahubali', duration_in_min=125, id=1)
        City.objects.create(name='Hyderabad', id=1)
        Theatre.objects.create(name='Icon Hitech', city_id=1, number_of_screens=5, id=1)
        Screen.objects.create(screen_number=1, theatre_id=1, id=1)
        Show.objects.create(id=1, movie_id=1, screen_id=1,
                            show_start_time=timezone.now(), show_end_time=timezone.now())
        User.objects.create(username='lauren', email='lauren@gmail.com', password='lauren123')
