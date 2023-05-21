import tkinter as tk
import unittest
from unittest.mock import Mock, patch, MagicMock, call

import ui.admin.views.students_view as view
from ui.admin.forms.students.add_students import handle


class TestAddStudentForm(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()

    @patch('repositories.student_repo.connection')
    def test_handle(self, mock_conn_students):
        view.AddStudentForm(self.root)

        first_name = "Alice"
        last_name = "Smith"
        year = 1
        semi_year = "A"
        student_group = 101

        students = [
            (5, "Alice", "Smith", 1, 1, 1),
            (6, "Bob", "Jones", 1, 1, 1),
            (7, "Adrian", "Smau", 1, 1, 2),
            (8, "Rares", "Gramescu", 1, 1, 2)
        ]

        mock_cursor_students = MagicMock()
        mock_cursor_students.fetchall.return_value = students
        mock_conn_students.return_value.cursor.return_value = mock_cursor_students
        mock_conn_students.return_value.closed = 1

        handle(first_name_entry=tk.StringVar(value=first_name), last_name_entry=tk.StringVar(value=last_name),
               study_year_var=tk.StringVar(value=year), semi_year_var=tk.StringVar(value=semi_year),
               student_group_var=tk.StringVar(value=str(student_group)))

        expected_calls = [
            call(
                'INSERT INTO student (first_name, last_name, study_year_id, semi_year_id, student_group_id) VALUES ('
                '%s, %s, %s, %s, %s)',
                ('Alice', 'Smith', '1', '1', '1')),
            call('SELECT * FROM student')
        ]

        mock_cursor_students.execute.assert_has_calls(expected_calls)

    @patch('repositories.student_repo.connection')
    def test_fetch_added_student(self, mock_conn_students):
        form = view.AddStudentForm(self.root)

        mock_master = Mock()
        form.master = mock_master

        expected_students = [
            (5, "Alice", "Smith", 1, 1, 1),
            (6, "Bob", "Jones", 1, 1, 1),
            (7, "Adrian", "Smau", 1, 1, 2),
            (8, "Rares", "Gramescu", 1, 1, 2)
        ]

        mock_cursor_students = MagicMock()
        mock_cursor_students.fetchall.return_value = expected_students
        mock_conn_students.return_value.cursor.return_value = mock_cursor_students
        mock_conn_students.return_value.closed = 1
        form.students_view = view.StudentsView(self.root)
        form.students_view.set_students(expected_students)

        form.go_back()

        current_frame = self.root.winfo_children()[-1]

        self.assertIsInstance(current_frame, view.StudentsView)

        updated_students = form.students_view.students
        self.assertEqual(len(updated_students), len(expected_students))
        for index in range(len(updated_students)):
            self.assertEqual(updated_students[index].first_name, expected_students[index][1])
