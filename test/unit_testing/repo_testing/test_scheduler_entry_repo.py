import unittest
from unittest.mock import MagicMock, patch

from repositories.scheduler_entry_repo import add_entry, get_entry_by_id, get_entries


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


class SchedulerEntryTesting(unittest.TestCase):
    @patch('repositories.scheduler_entry_repo.connection')
    @patch('repositories.scheduler_entry_repo.get_weekday_id')
    @patch('repositories.scheduler_entry_repo.get_time_slot_id')
    @patch('repositories.scheduler_entry_repo.get_teacher_id')
    @patch('repositories.scheduler_entry_repo.get_discipline_id')
    @patch('repositories.scheduler_entry_repo.get_study_year_id')
    @patch('repositories.scheduler_entry_repo.get_semi_year_id')
    @patch('repositories.scheduler_entry_repo.get_student_group_id')
    def test_given_scheduler_entry_repo_when_add_entry_then_successful(self, mock_student_group_method,
                                                                       mock_semi_year_method,
                                                                       mock_study_year_method,
                                                                       mock_discipline_method,
                                                                       mock_teacher_method,
                                                                       mock_time_slot_method,
                                                                       mock_weekday_method,
                                                                       mock_conn):
        mock_cursor = MagicMock()
        mock_conn.return_value.cursor.return_value = mock_cursor
        mock_teacher_method.side_effect = teacher_method_side_effect_2
        mock_study_year_method.side_effect = study_year_method_side_effect_2
        mock_student_group_method.side_effect = get_student_group_name_side_effect
        mock_semi_year_method.side_effect = get_semiyear_name_side_effect
        mock_time_slot_method.side_effect = get_timeslot_name_side_effect
        mock_discipline_method.side_effect = get_discipline_name_side_effect
        mock_weekday_method.side_effect = get_weekday_name_side_effect
        mock_conn.return_value.closed = 1

        add_entry("Monday", 8, 10, "John Smith", "SD", 1, "A", 101, 1)

        mock_conn.assert_called_once()
        mock_cursor.execute.assert_called_once_with(
            "INSERT INTO schedulerentry (weekday_id, time_slot_id, teacher_id, discipline_id, study_year_id,"
            " semi_year_id, student_group_id, scheduler_id) VALUES (%s, %s, "
            "%s, %s, %s, %s, %s, %s)",
            (1, 1, 1, 1, 1, 1, 1, 1))
        mock_cursor.close.assert_called_once()
        mock_teacher_method.assert_any_call("John Smith")
        mock_study_year_method.assert_any_call(1)
        mock_student_group_method.assert_any_call(101)
        mock_semi_year_method.assert_any_call("A")
        mock_time_slot_method.assert_any_call(8, 10)
        mock_discipline_method.assert_any_call("SD")
        mock_weekday_method.assert_any_call("Monday")
        mock_study_year_method.assert_any_call(1)

    @patch('repositories.scheduler_entry_repo.connection')
    @patch('repositories.scheduler_entry_repo.get_weekday_id')
    @patch('repositories.scheduler_entry_repo.get_time_slot_id')
    @patch('repositories.scheduler_entry_repo.get_teacher_id')
    @patch('repositories.scheduler_entry_repo.get_discipline_id')
    @patch('repositories.scheduler_entry_repo.get_study_year_id')
    @patch('repositories.scheduler_entry_repo.get_semi_year_id')
    @patch('repositories.scheduler_entry_repo.get_student_group_id')
    def test_given_scheduler_entry_repo_and_index_error_given_when_add_entry_then_throw_index_error(self,
                                                                                                    mock_student_group_method,
                                                                                                    mock_semi_year_method,
                                                                                                    mock_study_year_method,
                                                                                                    mock_discipline_method,
                                                                                                    mock_teacher_method,
                                                                                                    mock_time_slot_method,
                                                                                                    mock_weekday_method,
                                                                                                    mock_conn):
        mock_cursor = MagicMock()
        mock_conn.return_value.cursor.return_value = mock_cursor
        mock_conn.return_value.closed = 1
        mock_teacher_method.side_effect = teacher_method_side_effect_2
        mock_study_year_method.side_effect = study_year_method_side_effect_2
        mock_student_group_method.side_effect = side_effect_error
        mock_semi_year_method.side_effect = get_semiyear_name_side_effect
        mock_time_slot_method.side_effect = get_timeslot_name_side_effect
        mock_discipline_method.side_effect = get_discipline_name_side_effect
        mock_weekday_method.side_effect = get_weekday_name_side_effect

        with self.assertRaises(IndexError):
            add_entry("Monday", 8, 10, "John Smith", "SD", 1, "A", 101, 1)

        mock_conn.assert_called_once()
        mock_teacher_method.assert_any_call("John Smith")
        mock_study_year_method.assert_any_call(1)
        mock_semi_year_method.assert_any_call("A")
        mock_time_slot_method.assert_any_call(8, 10)
        mock_discipline_method.assert_any_call("SD")
        mock_weekday_method.assert_any_call("Monday")
        mock_study_year_method.assert_any_call(1)

    @patch('repositories.scheduler_entry_repo.connection')
    def test_given_scheduler_entry_repo_when_get_entry_by_id_then_successful(self, mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [([8, 10],)]
        mock_conn.return_value.closed = 1
        mock_conn.return_value.cursor.return_value = mock_cursor

        result = get_entry_by_id(1)

        self.assertEqual([8, 10], result)
        mock_conn.assert_called_once()
        mock_cursor.execute.assert_called_once_with(
            "SELECT id FROM timeslot WHERE entry_id=%s", (1,))
        mock_cursor.fetchall.assert_called_once()
        mock_cursor.close.assert_called_once()

    @patch('repositories.scheduler_entry_repo.connection')
    @patch('repositories.scheduler_entry_repo.get_weekday_name')
    @patch('repositories.scheduler_entry_repo.get_time_slot')
    @patch('repositories.scheduler_entry_repo.get_teacher_full_name')
    @patch('repositories.scheduler_entry_repo.get_discipline_name')
    @patch('repositories.scheduler_entry_repo.get_study_year_number')
    @patch('repositories.scheduler_entry_repo.get_semi_year_name')
    @patch('repositories.scheduler_entry_repo.get_student_group_name')
    def test_given_scheduler_entry_repo_when_get_entry_then_successful(self, mock_student_group_method,
                                                                       mock_semi_year_method,
                                                                       mock_study_year_method,
                                                                       mock_discipline_method,
                                                                       mock_teacher_method,
                                                                       mock_time_slot_method,
                                                                       mock_weekday_method,
                                                                       mock_conn):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(1, 1, 1, 1, 1, 1, 1, 1, 1,)]
        mock_conn.return_value.closed = 1
        mock_conn.return_value.cursor.return_value = mock_cursor
        mock_teacher_method.side_effect = teacher_method_side_effect
        mock_study_year_method.side_effect = study_year_method_side_effect
        mock_student_group_method.side_effect = get_student_group_id_side_effect
        mock_semi_year_method.side_effect = get_semiyear_id_side_effect
        mock_time_slot_method.side_effect = get_timeslot_id_side_effect
        mock_discipline_method.side_effect = get_discipline_id_side_effect
        mock_weekday_method.side_effect = get_weekday_id_side_effect

        result = get_entries()

        self.assertEqual(len(result), 1)
        self.assertEqual(1, result[0][0])
        self.assertEqual("Monday", result[0][1])
        self.assertEqual([8, 10], result[0][2])
        self.assertEqual("SD", result[0][4])
        self.assertEqual(1, result[0][5])
        self.assertEqual("A", result[0][6])
        self.assertEqual(101, result[0][7])
        self.assertEqual("John Smith", result[0][3])
        mock_conn.assert_called_once()
        mock_cursor.execute.assert_called_once_with(
            "SELECT * FROM schedulerentry")
        mock_cursor.close.assert_called_once()
        mock_teacher_method.assert_any_call(1)
        mock_study_year_method.assert_any_call(1)
        mock_student_group_method.assert_any_call(1)
        mock_semi_year_method.assert_any_call(1)
        mock_time_slot_method.assert_any_call(1)
        mock_discipline_method.assert_any_call(1)
        mock_weekday_method.assert_any_call(1)
        mock_study_year_method.assert_any_call(1)
        mock_cursor.fetchall.assert_called_once()
        mock_cursor.close.assert_called_once()
