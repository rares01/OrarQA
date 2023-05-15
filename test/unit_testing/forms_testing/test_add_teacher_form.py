import tkinter as tk
import unittest
from unittest.mock import Mock, patch, MagicMock
from ui.admin.views import disciplines_view
from ui.admin.views.disciplines_view import DisciplinesView
from ui.admin.views.teachers_view import TeachersView, AddTeacherForm


class TestAddTeacherForm(unittest.TestCase):
    def setUp(self):
        # Create a root window for test
        self.root = tk.Tk()

    @patch('repositories.teacher_repo.connection')
    def test_handle(self, mock_conn_teacher):
        # Test the handle method to add a discipline
        # Assert that the discipline is added correctly

        # Create an instance of AddDisciplineForm
        form = AddTeacherForm(self.root)

        # Set up the test data
        first_name = "Ionut"
        last_name = "Andrei"

        teachers = [
            (1, "Jane", "Smith"),
            (2, "John", "Doe"),
        ]

        mock_cursor_teacher = MagicMock()
        mock_cursor_teacher.fetchall.return_value = teachers
        mock_conn_teacher.return_value.cursor.return_value = mock_cursor_teacher

        # Call the handle method
        form.handle(first_name_entry=tk.StringVar(value=first_name), last_name_entry=tk.StringVar(value=last_name))

        mock_cursor_teacher.execute.assert_called_once_with(
            "INSERT INTO teacher (first_name, last_name) VALUES (%s,%s)",
            ('Ionut', 'Andrei',))

    # @patch('repositories.teacher_repo.connection')
    # def test_fetch_added_teacher(self, mock_conn_teacher):
    #     # Test the go_back method to navigate back to the disciplines view
    #     # Assert that the disciplines view is displayed and the disciplines are updated
    #
    #     # Create an instance of AddDisciplineForm
    #     form = AddTeacherForm(self.root)
    #
    #     # Create a mock master
    #     mock_master = Mock()
    #
    #     # Set the view's master to the mock master
    #     form.master = mock_master
    #
    #     teachers = [
    #         (1, "Jane", "Smith"),
    #         (2, "John", "Doe"),
    #     ]
    #
    #     mock_cursor_teacher = MagicMock()
    #     mock_cursor_teacher.fetchall.return_value = teachers
    #     mock_conn_teacher.return_value.cursor.return_value = mock_cursor_teacher
    #     form.teachers_view = TeachersView(self.root)
    #
    #     # Call the go_back method
    #     form.go_back()
    #
    #     # Get the current frame
    #     current_frame = self.root.winfo_children()[-1]
    #
    #     # Assert that the current frame is the disciplines view
    #     self.assertIsInstance(current_frame, TeachersView)
    #
    #     # Assert that the disciplines are updated in the view
    #     updated_teachers = teachers
    #     self.assertEqual(len(teachers), len(updated_teachers))
    #     for index in range(len(updated_teachers)):
    #         self.assertEqual(updated_teachers[index].name, teachers[index][1])
