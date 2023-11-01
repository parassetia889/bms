from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from bms_models.models import BookedSeat, Booking, Show, Seat


class BookSeat:

    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def book_seat(request):

        show_id = request.POST['show']
        seats = request.POST['seat']
        seat_list = seats.split(',')

        screen_id = Show.objects.get(id=show_id).screen_id

        seat_id = list(Seat.objects.filter(seat_number__in=seat_list,
                       screen_id=screen_id).values_list('id', flat=True))

        is_booked = BookedSeat.objects.filter(
            show_id=show_id, seat_id__in=seat_id).values_list('id', flat=True)

        if len(is_booked) > 0:
            return JsonResponse({"Response": "One or more given seats are already booked"})

        update_booking = Booking(user_id=1, show_id=show_id, number_of_seats_booked=len(seat_list))
        update_booking.save()
        booking_id = update_booking.id

        for seat in seat_id:
            book_seat = BookedSeat(seat_id=seat, show_id=show_id, booking_id=booking_id)
            book_seat.save()

        return JsonResponse({"Response": "Seat booking successful"})
