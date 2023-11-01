from datetime import datetime


class HealthCheckDTO():
    current_beat: datetime

    """assigning the argument passed during the object creation to the current_beat"""

    def __init__(self, current_beat: datetime):
        self.current_beat = current_beat
