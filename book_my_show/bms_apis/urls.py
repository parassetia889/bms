from django.urls import path
from .main_apis.movie_from_theatre import MoviesListFromTheatre
from .main_apis.movie_from_city import MovieFromCity
from .main_apis.theatre_from_city import TheatreFromCity
from .main_apis.shows_for_a_movie_in_a_theatre import ShowsForAMovieInATheatre
from .main_apis.available_seats_from_show import AvailableSeatsFromShow
from .main_apis.book_seat import BookSeat


urlpatterns = [
    path('get_movie_from_theatre/', MoviesListFromTheatre.get_movie_from_theatre),
    path('get_movie_from_city/', MovieFromCity.get_movie_from_city),
    path('get_theatre_from_city/', TheatreFromCity.get_theatre_from_city),
    path('get_show_from_movie_and_theatre/', ShowsForAMovieInATheatre.shows_for_a_movie_in_a_theatre),
    path('available_seats_from_show/', AvailableSeatsFromShow.available_seats_from_show),
    path('book_seat/', BookSeat.book_seat),
]
