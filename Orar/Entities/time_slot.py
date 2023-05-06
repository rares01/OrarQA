class TimeSlot:
    def __init__(self, id: int, start_hour: int, end_hour: int):
        self.id = id
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.scheduled_entries = []
