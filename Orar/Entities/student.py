from Entities.semi_year import SemiYear
from Entities.study_year import StudyYear


class Student:
    def __init__(self, id: int, first_name: str, last_name: str, study_year: StudyYear, semi_year: SemiYear,
                 group_id: int):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.study_year = study_year
        self.semi_year = semi_year
        self.group_id = group_id
