import tkinter as tk
import unittest
from unittest.mock import patch, MagicMock, call

from ui.admin.forms.timetable.add_timetable_entry import handle


def get_weekday_id_side_effect(weekday_id):
    if weekday_id == 1:
        return 'Monday'
    elif weekday_id == 2:
        return 'Tuesday'
    elif weekday_id == 3:
        return 'Wednesday'
    elif weekday_id == 4:
        return 'Thursday'
    else:
        return 'Friday'


def get_weekday_name_side_effect(weekday_name):
    if weekday_name == 'Monday':
        return 1
    elif weekday_name == 'Tuesday':
        return 2
    elif weekday_name == 'Wednesday':
        return 3
    elif weekday_name == 'Thursday':
        return 4
    else:
        return 5


def get_timeslot_id_side_effect(timeslot_id):
    if timeslot_id == 1:
        return [8, 10]
    else:
        return [10, 12]


def get_timeslot_name_side_effect(start_date, end_date):
    if start_date == 8 and end_date == 10:
        return 1
    else:
        return 2


def get_discipline_id_side_effect(discipline_id):
    if discipline_id == 1:
        return "SD"
    else:
        return "IP"


def get_discipline_name_side_effect(discipline_name):
    if discipline_name == "SD":
        return 1
    else:
        return 2


def get_semiyear_id_side_effect(semiyear_id):
    if semiyear_id == 1:
        return "A"
    else:
        return "B"


def get_semiyear_name_side_effect(semiyear_name):
    if semiyear_name == "A":
        return 1
    else:
        return 2


def get_student_group_id_side_effect(student_group_id):
    if student_group_id == 1:
        return 101
    else:
        return 102


def get_student_group_name_side_effect(student_group_name):
    if student_group_name == 101:
        return 1
    else:
        return 2


def teacher_method_side_effect(teacher_id):
    if teacher_id == 1:
        return 'John Smith'
    else:
        return 'Alice Smith'


def teacher_method_side_effect_2(teacher_value):
    if teacher_value == 'John Smith':
        return 1
    else:
        return 2


def side_effect_error(id):
    raise IndexError("Index Error")


def study_year_method_side_effect(study_year_id):
    if study_year_id == 1:
        return 1
    else:
        return 2


def study_year_method_side_effect_2(study_year_value):
    if study_year_value == 1:
        return 1
    else:
        return 2


def get_teacher_id_side_effect(full_name):
    return 1


class TestAddTimetableEntryForm(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()

    @patch('repositories.scheduler_entry_repo.connection')
    @patch('repositories.scheduler_entry_repo.get_weekday_name')
    @patch('repositories.scheduler_entry_repo.get_time_slot')
    @patch('repositories.scheduler_entry_repo.get_teacher_full_name')
    @patch('repositories.scheduler_entry_repo.get_discipline_name')
    @patch('repositories.scheduler_entry_repo.get_study_year_number')
    @patch('repositories.scheduler_entry_repo.get_semi_year_name')
    @patch('repositories.scheduler_entry_repo.get_student_group_name')
    @patch('repositories.teacher_repo.connection')
    def test_handle(self, mock_teacher_connection, mock_student_group_method,
                    mock_semi_year_method,
                    mock_study_year_method,
                    mock_discipline_method,
                    mock_teacher_method,
                    mock_time_slot_method,
                    mock_weekday_method,
                    mock_conn):
        weekday = "Friday"
        time_slot = "8:00-10:00"
        teacher = "John Smith"
        discipline = "IP"
        study_year = "1"
        semi_year = "A"
        student_group = "101"

        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(8, "Friday", 8, 10, "John Smith", "IP", 1, "A", 101, 1)]
        mock_conn.return_value.closed = 1
        mock_conn.return_value.cursor.return_value = mock_cursor
        mock_teacher_method.side_effect = teacher_method_side_effect
        mock_study_year_method.side_effect = study_year_method_side_effect
        mock_student_group_method.side_effect = get_student_group_id_side_effect
        mock_semi_year_method.side_effect = get_semiyear_id_side_effect
        mock_time_slot_method.side_effect = get_timeslot_id_side_effect
        mock_discipline_method.side_effect = get_discipline_id_side_effect
        mock_weekday_method.side_effect = get_weekday_id_side_effect

        teachers = [
            (1, "Jane", "Smith"),
            (2, "John", "Doe"),
            (3, "Jane", "Smith"),
            (4, "John", "Doe")
        ]

        mock_cursor_teachers = MagicMock()
        mock_cursor_teachers.fetchall.return_value = teachers
        mock_teacher_connection.return_value.cursor.return_value = mock_cursor_teachers
        mock_teacher_connection.return_value.closed = 1

        handle(weekday_entry=tk.StringVar(value=weekday), time_slot_entry=tk.StringVar(value=time_slot),
               teacher_entry=tk.StringVar(value=teacher), discipline_entry=tk.StringVar(value=discipline),
               study_year_entry=tk.StringVar(value=study_year), semi_year_entry=tk.StringVar(value=semi_year),
               student_group_entry=tk.StringVar(value=student_group))

        expected_calls = [
            call('INSERT INTO schedulerentry (weekday_id, time_slot_id, teacher_id, discipline_id, study_year_id, '
                 'semi_year_id, student_group_id, scheduler_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', (5, 1, 1,
                                                                                                           2, 1, 1,
                                                                                                           1, 1)),
            call('SELECT * FROM schedulerentry')
        ]

        mock_cursor.execute.assert_has_calls(expected_calls)
