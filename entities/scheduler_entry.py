from entities.study_year import StudyYear
from entities.time_slot import TimeSlot
from entities.weekday import Weekday


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


scheduler_entries = [
    SchedulerEntry(1, 'Monday', '09:00 - 11:00', 'John Doe', 'Mathematics', 2, 'Second', 1, 1),
    SchedulerEntry(2, 'Tuesday', '11:00 - 13:00', 'Jane Smith', 'English', 3, 'First', 2, 1),
    SchedulerEntry(3, 'Wednesday', '13:00 - 15:00', 'Bob Johnson', 'Physics', 2, 'Second', 1, 1),
]

# Generate HTML table with scheduler entries
html = '<!DOCTYPE html>'

html += '<html>\n'
html += '<body>\n'

html += '<table>\n'
html += '<tr><th>ID</th><th>Weekday</th><th>Time Slot</th><th>Teacher</th><th>Discipline</th>'
html += '<th>Study Year</th><th>Semi Year</th><th>Student Group</th><th>Scheduler ID</th></tr>\n'
for entry in scheduler_entries:
    html += f'<tr><td>{entry.id}</td><td>{entry.weekday}</td><td>{entry.time_slot}</td>'
    html += f'<td>{entry.teacher_id}</td><td>{entry.discipline}</td><td>{entry.study_year_id}</td>'
    html += f'<td>{entry.semi_year}</td><td>{entry.student_group}</td><td>{entry.scheduler_id}</td></tr>\n'
html += '</table>'

html += '</body>\n'
html += '</html>\n'

print(html)