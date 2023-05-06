from Entities.study_year import StudyYear
from Entities.time_slot import TimeSlot
from Entities.weekday import Weekday


class SchedulerEntry:
    def __init__(self, id: int, weekday_id: int, time_slot_id: id, teacher_id: int, discipline_id: int,
                 blocked: bool, study_year_id: int, semi_year_id: int, group_id: int, scheduler_id:int ):
        self.id = id
        self.weekday_id = weekday_id
        self.time_slot_id = time_slot_id
        self.teacher_id = teacher_id
        self.discipline = discipline_id
        self.blocked = blocked
        self.study_year_id = study_year_id
        self.semi_year = semi_year_id
        self.group_id = group_id

