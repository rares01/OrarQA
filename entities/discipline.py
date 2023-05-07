class Discipline:
    def __init__(self, id: int, name: str, study_year: int, teacher_full_name: str):
        self.id = id
        self.name = name
        self.study_year = study_year
        self.teacher_full_name = teacher_full_name
        self.scheduler_entries = []
