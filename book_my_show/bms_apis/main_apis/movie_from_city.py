from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from bms_models.models import Movie, City, Screen, Theatre, Show


class MovieFromCity():
    @api_view(["GET"])
    @permission_classes([IsAuthenticated])
    def get_movie_from_city(request):

        city_name = request.GET.get('name')

        try:
            city_id = City.objects.get(name__iexact=city_name).id
        except City.DoesNotExist:
            city_id = -1

        if city_id == -1:
            return JsonResponse({"Response ": "No Matching Record Found"})

        theatre_list = list(Theatre.objects.filter(city_id=city_id).values_list('id', flat=True))
        screen_list = list(Screen.objects.filter(
            theatre_id__in=theatre_list).values_list('id', flat=True))
        movie_list = list(Show.objects.filter(
            screen_id__in=screen_list).values_list('movie_id', flat=True))
        movie_list = list(set(movie_list))
        movie_names = list(Movie.objects.filter(id__in=movie_list).values_list('name', flat=True))

        return JsonResponse({'Movies  ': movie_names})
