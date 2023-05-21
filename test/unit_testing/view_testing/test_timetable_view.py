import unittest
from tkinter import ttk
import tkinter as tk
from unittest.mock import Mock, patch, MagicMock
import ui.home.home_page as home

from ui.admin.views.timetable_view import TimetableView


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


class TestTimetableView(unittest.TestCase):
    def setUp(self):
        root = tk.Tk()
        self.view = TimetableView(root)

    @patch('repositories.scheduler_entry_repo.connection')
    @patch('repositories.scheduler_entry_repo.get_weekday_name')
    @patch('repositories.scheduler_entry_repo.get_time_slot')
    @patch('repositories.scheduler_entry_repo.get_teacher_full_name')
    @patch('repositories.scheduler_entry_repo.get_discipline_name')
    @patch('repositories.scheduler_entry_repo.get_study_year_number')
    @patch('repositories.scheduler_entry_repo.get_semi_year_name')
    @patch('repositories.scheduler_entry_repo.get_student_group_name')
    def test_display(self, mock_student_group_method,
                     mock_semi_year_method,
                     mock_study_year_method,
                     mock_discipline_method,
                     mock_teacher_method,
                     mock_time_slot_method,
                     mock_weekday_method,
                     mock_conn):
        mock_cursor = MagicMock()
        entries = [
            [1, 'Friday', '10 12', 'Alice Smith', 'IP', 1, 'B', 102]
        ]
        mock_conn.return_value.closed = 1
        mock_cursor.fetchall.return_value = entries
        mock_conn.return_value.cursor.return_value = mock_cursor
        mock_teacher_method.side_effect = teacher_method_side_effect
        mock_study_year_method.side_effect = study_year_method_side_effect
        mock_student_group_method.side_effect = get_student_group_id_side_effect
        mock_semi_year_method.side_effect = get_semiyear_id_side_effect
        mock_time_slot_method.side_effect = get_timeslot_id_side_effect
        mock_discipline_method.side_effect = get_discipline_id_side_effect
        mock_weekday_method.side_effect = get_weekday_id_side_effect

        self.view.display()
        tree_items = self.view.tree.get_children()
        for i, entry in enumerate(entries):
            item_values = self.view.tree.item(tree_items[i])['values']
            self.assertEqual(list(item_values), list(entry))

        self.assertIsInstance(self.view.tree, ttk.Treeview)
        self.assertIsInstance(self.view.add_button, ttk.Button)
        self.assertIsInstance(self.view.back_button, ttk.Button)
        self.assertIsInstance(self.view.generate_html, ttk.Button)
        self.assertIsInstance(self.view.weekday_filter, ttk.Combobox)
        self.assertIsInstance(self.view.time_slot_filter, ttk.Combobox)
        self.assertIsInstance(self.view.teacher_filter, ttk.Combobox)
        self.assertIsInstance(self.view.discipline_filter, ttk.Combobox)
        self.assertIsInstance(self.view.study_year_filter, ttk.Combobox)
        self.assertIsInstance(self.view.semi_year_filter, ttk.Combobox)
        self.assertIsInstance(self.view.group_filter, ttk.Combobox)

    def test_go_back(self):
        self.view.master.switch_frame = Mock()

        self.view.go_back()

        self.view.master.switch_frame.assert_called_with(home.HomePage)
