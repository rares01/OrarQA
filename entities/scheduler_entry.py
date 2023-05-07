from entities.study_year import StudyYear
from entities.time_slot import TimeSlot
from entities.weekday import Weekday


class SchedulerEntry:
    def __init__(self, id: int, weekday_id: int, time_slot_id: id, teacher_id: int, discipline_id: int,
                 study_year_id: int, semi_year_id: int, student_group_id: int, scheduler_id: int):
        self.id = id
        self.weekday_id = weekday_id
        self.time_slot_id = time_slot_id
        self.teacher_id = teacher_id
        self.discipline = discipline_id
        self.study_year_id = study_year_id
        self.semi_year = semi_year_id
        self.student_group_id = student_group_id
        self.scheduler_id = scheduler_id
