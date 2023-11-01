from bms_models.models import City, Theatre
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes


class TheatreFromCity:
    @api_view(['GET'])
    @permission_classes([IsAuthenticated])
    def get_theatre_from_city(request):

        city_name = request.GET.get('name').lower()

        city_id = -1

        try:
            city_id = City.objects.get(name__iexact=city_name).id

        except City.DoesNotExist:
            city_id = -1

        if city_id == -1:
            return JsonResponse({"Response": "No Match Found"})

        else:
            querySet = Theatre.objects.filter(city_id=city_id)
            theatre_names = list(querySet.values_list('name', flat=True))

            return JsonResponse({"Theatres": theatre_names})
