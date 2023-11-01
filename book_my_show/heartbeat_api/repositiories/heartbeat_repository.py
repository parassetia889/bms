from datetime import datetime
from ..dto.heartbeat_dto import HealthCheckDTO


class HealthCheckRepository:

    """creaitng the object of the dto and passing the current date time to it"""

    def healthCheck(self) -> HealthCheckDTO:
        return HealthCheckDTO(datetime.now()).current_beat
