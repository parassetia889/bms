from bms_models.models import Account, BookedSeat, Booking, City, Movie, Screen, Seat, Show, Theatre, User
from django.contrib import admin

# Register your models here.
admin.site.register(Movie)
admin.site.register(City)
admin.site.register(Screen)
admin.site.register(Show)
admin.site.register(Theatre)
admin.site.register(Booking)
admin.site.register(BookedSeat)
admin.site.register(Seat)
admin.site.register(User)
admin.site.register(Account)
