from django.http import HttpResponse, JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from bms_models.models import Theatre, Screen, Show, Movie
from django.core import serializers


class ShowsForAMovieInATheatre:

    @api_view(['GET'])
    @permission_classes([IsAuthenticated])
    def shows_for_a_movie_in_a_theatre(request):

        movie_name = request.GET.get('movie')
        theatre_name = request.GET.get('theatre')

        try:
            theatre_id = Theatre.objects.get(name__iexact=theatre_name).id
        except Theatre.DoesNotExist:
            return JsonResponse({"Response": "Theatre Not Found"})

        try:
            movie_id = Movie.objects.get(name__iexact=movie_name).id
        except Movie.DoesNotExist:
            return JsonResponse({"Response": "Movie Not Found"})

        screen_id_list = list(Screen.objects.filter(
            theatre_id=theatre_id).values_list('id', flat=True))
        shows = Show.objects.filter(movie_id=movie_id,
                                    screen_id__in=screen_id_list)
        shows_json = serializers.serialize('json', shows)

        return HttpResponse(shows_json, content_type='application/json')
