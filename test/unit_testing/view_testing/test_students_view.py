import tkinter as tk
import unittest
from tkinter import ttk
from unittest.mock import Mock, patch, MagicMock

import ui.admin.admin_page as admin
import ui.admin.views.students_view as students_view_module
from ui.admin.forms.students.add_students import AddStudentForm


class TestStudentsView(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up any required test data or dependencies for the entire test class
        cls.root = tk.Tk()

    def setUp(self):
        self.view = students_view_module.StudentsView(self.root)

    @patch('repositories.student_repo.connection')
    def test_display(self, mock_conn_student):
        students = [
            (5, "Alice", "Smith", 1, 1, 1),
            (6, "Bob", "Jones", 1, 1, 1),
            (7, "Adrian", "Smau", 1, 1, 1),
            (8, "Rares", "Gramescu", 1, 1, 2)
        ]

        mock_cursor_student = MagicMock()
        mock_cursor_student.fetchall.return_value = students
        mock_conn_student.return_value.cursor.return_value = mock_cursor_student
        mock_conn_student.return_value.closed = 1

        self.view.display()

        tree_items = self.view.tree.get_children()
        for i, student in enumerate(students):
            item_values = self.view.tree.item(tree_items[i])['values']
            self.assertEqual(item_values[0], student[0])
            self.assertEqual(item_values[1], student[1])
            self.assertEqual(item_values[2], student[2])

        self.assertIsInstance(self.view.tree, ttk.Treeview)
        self.assertIsInstance(self.view.add_button, ttk.Button)
        self.assertIsInstance(self.view.delete_button, ttk.Button)
        self.assertIsInstance(self.view.back_button, ttk.Button)
        self.assertIsInstance(self.view.semi_year_filter, ttk.Combobox)
        self.assertIsInstance(self.view.group_filter, ttk.Combobox)
        self.assertIsInstance(self.view.study_year_filter, ttk.Combobox)

        self.assertEqual(len(self.view.tree.get_children()), len(students_view_module.get_students()))
        self.assertEqual(str(self.view.delete_button["state"]), "disabled")
        self.assertEqual(self.view.semi_year_filter.get(), "All")
        self.assertEqual(self.view.group_filter.get(), "All")
        self.assertEqual(self.view.study_year_filter.get(), "All")

    def test_on_tree_select(self):
        selected_item = self.view.tree.get_children()[0]
        self.view.tree.selection_set(selected_item)

        self.view.on_tree_select(Mock())

        self.assertEqual(str(self.view.delete_button["state"]), "enabled")

    def test_on_tree_select_no_selection(self):
        self.view.tree.selection_clear()

        self.view.on_tree_select(Mock())

        self.assertEqual(str(self.view.delete_button["state"]), "disabled")

    @patch('repositories.student_repo.connection')
    def test_apply_filters(self, mock_conn_student):
        students = [
            (5, "Alice", "Smith", 1, 1, 1),
            (6, "Bob", "Jones", 1, 1, 1),
            (7, "Adrian", "Smau", 1, 1, 1),
            (8, "Rares", "Gramescu", 1, 1, 2)
        ]

        mock_cursor_student = MagicMock()
        mock_cursor_student.fetchall.return_value = students
        mock_conn_student.return_value.cursor.return_value = mock_cursor_student
        mock_conn_student.return_value.closed = 1

        self.view.students = students_view_module.get_students()
        for student in self.view.students:
            self.view.tree.insert("", "end", values=(
                student.id, student.first_name, student.last_name, student.study_year, student.semi_year,
                student.student_group))

        self.view.study_year_filter.set("1")
        self.view.semi_year_filter.set("A")
        self.view.group_filter.set("All")
        self.view.apply_filters()

        expected_filtered_students = [
            self.view.students[0],
            self.view.students[1]
        ]

        self.assertEqual(len(self.view.tree.get_children()), len(students))
        for i, student in enumerate(expected_filtered_students):
            values = self.view.tree.item(self.view.tree.get_children()[i])['values']
            self.assertEqual(values[0], student.id)
            self.assertEqual(values[1], student.first_name)
            self.assertEqual(values[2], student.last_name)
            self.assertEqual(values[3], student.study_year)
            self.assertEqual(values[4], student.semi_year)
            self.assertEqual(values[5], student.student_group)

    def test_add_student(self):
        self.view.master.switch_frame = Mock()

        self.view.add_student()

        self.view.master.switch_frame.assert_called_with(AddStudentForm)

    def test_go_back(self):
        self.view.master.switch_frame = Mock()

        self.view.go_back()

        self.view.master.switch_frame.assert_called_with(admin.AdminPage)

    @patch('repositories.student_repo.connection')
    def test_delete_student(self, mock_conn_student):

        students = [
            (5, "Alice", "Smith", 1, 1, 1),
            (6, "Bob", "Jones", 1, 1, 1),
            (7, "Adrian", "Smau", 1, 1, 1),
            (8, "Rares", "Gramescu", 1, 1, 2)
        ]

        mock_cursor_student = MagicMock()
        mock_cursor_student.fetchall.return_value = students
        mock_conn_student.return_value.cursor.return_value = mock_cursor_student
        mock_conn_student.return_value.closed = 1

        self.view.students = students
        self.view.tree.selection_set(self.view.tree.get_children()[0])
        mock_cursor_student = MagicMock()
        mock_cursor_student.fetchall.return_value = students[1:]
        mock_conn_student.return_value.cursor.return_value = mock_cursor_student
        self.view.delete_student()
        self.assertEqual(len(self.view.tree.get_children()), len(students) - 1)

