import tkinter as tk
import unittest
from unittest.mock import Mock, patch, MagicMock

import ui.admin.views.students_view as view
from ui.admin.forms.students.add_students import handle


class TestAddStudentForm(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()

    @patch('repositories.student_repo.connection')
    def test_handle(self, mock_conn_students):
        form = view.AddStudentForm(self.root)

        first_name = "John"
        last_name = "Doe"
        year = 1
        semi_year = 1
        student_group = 1

        students = [
            (5, "Alice", "Smith", 1, "A", 101),
            (6, "Bob", "Jones", 1, "A", 101),
            (7, "Adrian", "Smau", 1, "A", 102),
            (8, "Rares", "Gramescu", 1, "A", 102)
        ]

        mock_cursor_students = MagicMock()
        mock_cursor_students.fetchall.return_value = students
        mock_conn_students.return_value.cursor.return_value = mock_cursor_students

        handle(first_name_entry=tk.StringVar(value=first_name), last_name_entry=tk.StringVar(value=last_name),
                    study_year_var=tk.StringVar(value=str(year)), semi_year_var=tk.StringVar(value=str(semi_year)),
                    student_group_var=tk.StringVar(value=str(student_group)))

        mock_cursor_students.execute.assert_called_once_with(
            "INSERT INTO student "
            "(first_name, last_name, study_year_id, semi_year_id, student_group_id) VALUES (%s,%s,%s,%s,%s)",
            ('John', 'Doe', 1, 1, 1))

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
        form.students_view = view.StudentsView(self.root)
        form.students_view.set_students(expected_students)

        form.go_back()

        current_frame = self.root.winfo_children()[-1]

        self.assertIsInstance(current_frame, view.StudentsView)

        updated_students = form.students_view.students
        self.assertEqual(len(updated_students), len(expected_students))
        for index in range(len(updated_students)):
            self.assertEqual(updated_students[index].first_name, expected_students[index][1])
