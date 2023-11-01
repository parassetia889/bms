import json
from django.http import JsonResponse
from ..services.heartbeat_service import HealthCheckService


class HealthCheckView:

    """getting the api call request and returing a json response"""
    def healthCheckView(request) -> json:
        return JsonResponse({'Last Recorded Beat  ': HealthCheckService().healthCheck()})
