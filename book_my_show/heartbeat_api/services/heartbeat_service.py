from ..repositiories.heartbeat_repository import HealthCheckRepository


class HealthCheckService:

    """creating the object of HealthCheckRepository and its function healthCheck and returning it"""

    def healthCheck(self):
        return HealthCheckRepository().healthCheck()
