from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from bms_models.models import Show, Movie, Theatre, Screen


class MoviesListFromTheatre:
    @api_view(['GET'])
    @permission_classes([IsAuthenticated])
    def get_movie_from_theatre(request):
        theatre_name = request.GET.get('name')
        try:
            theatre_id = Theatre.objects.get(name__iexact=theatre_name).id
        except Theatre.DoesNotExist:
            return JsonResponse({"Response": "No Theatre Found"})
        screen_id_list = list(Screen.objects.filter(
            theatre_id=theatre_id).values_list('id', flat=True))
        movie_id_list = list(Show.objects.filter(
            screen_id__in=screen_id_list).values_list('movie_id', flat=True))
        movie_id_list = list(set(movie_id_list))
        movie_names = list(Movie.objects.filter(
            id__in=movie_id_list).values_list('name', flat=True))
        return JsonResponse({'Movie Names': movie_names})
