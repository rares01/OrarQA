import tkinter as tk
import unittest
from unittest.mock import patch, MagicMock, call

from ui.admin.views.teachers_view import AddTeacherForm


class TestAddTeacherForm(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()

    @patch('repositories.teacher_repo.connection')
    def test_handle(self, mock_conn_teacher):
        form = AddTeacherForm(self.root)

        first_name = "John"
        last_name = "Doe"

        teachers = [
            (1, "Jane", "Smith"),
            (2, "John", "Doe"),
        ]

        mock_cursor_teacher = MagicMock()
        mock_cursor_teacher.fetchall.return_value = teachers
        mock_conn_teacher.return_value.cursor.return_value = mock_cursor_teacher
        mock_conn_teacher.return_value.closed = 1

        form.handle(first_name_entry=tk.StringVar(value=first_name), last_name_entry=tk.StringVar(value=last_name))

        expected_calls = [
            call('INSERT INTO teacher (first_name, last_name) VALUES (%s,%s)', ('John', 'Doe')),
            call('SELECT first_name, last_name FROM teacher')
        ]

        mock_cursor_teacher.execute.assert_has_calls(expected_calls)