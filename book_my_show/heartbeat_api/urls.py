from django.urls import path

from .views import heartbeat_view

urlpatterns = [path('', heartbeat_view.HealthCheckView.healthCheckView)]
