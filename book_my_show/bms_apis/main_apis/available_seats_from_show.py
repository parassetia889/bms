from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from bms_models.models import BookedSeat, Seat, Show


class AvailableSeatsFromShow:

    @api_view(['GET'])
    @permission_classes([IsAuthenticated])
    def available_seats_from_show(request):

        show_id = request.GET.get('show')

        screen_id = Show.objects.get(id=show_id).screen_id
        seats_list = list(Seat.objects.filter(screen_id=screen_id).values_list('id', flat=True))

        booked_seats_list = list(BookedSeat.objects.filter(
            show_id=show_id, seat__in=seats_list).values_list('seat_id', flat=True))

        available_seats_list = [i for i in seats_list if i not in booked_seats_list]

        available_seat_numbers = list(Seat.objects.filter(
            id__in=available_seats_list).values_list('seat_number', flat=True))

        return JsonResponse({"Available Seats": available_seat_numbers})
