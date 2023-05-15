class SchedulerEntry:
    def __init__(self, id: int, weekday: str, time_slot: str, teacher: str, discipline: str,
                 study_year: int, semi_year: str, student_group: int, scheduler_id: int):
        self.id = id
        self.weekday = weekday
        self.time_slot = time_slot
        self.teacher_id = teacher
        self.discipline = discipline
        self.study_year_id = study_year
        self.semi_year = semi_year
        self.student_group = student_group
        self.scheduler_id = scheduler_id
