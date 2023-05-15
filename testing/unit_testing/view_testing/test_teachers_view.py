import unittest
from tkinter import ttk
from unittest.mock import Mock, patch, MagicMock
import tkinter as tk
import ui.admin.admin_page as admin
from ui.admin.forms.teachers.add_teacher_form import AddTeacherForm
from ui.admin.views.teachers_view import TeachersView
from repositories.teacher_repo import add_teacher, get_teacher_id_by_full_name, \
    get_teacher_full_name_by_id


class TestTeachersView(unittest.TestCase):
    def setUp(self):
        root = tk.Tk()
        self.view = TeachersView(root)

    @patch('repositories.teacher_repo.connection')
    def test_display(self, mock_conn):

        # Create a mock teacher list
        teachers = [
            (1, "Jane", "Smith"),
            (2, "John", "Doe"),
            (3, "Jane", "Smith"),
            (4, "John", "Doe")
        ]

        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = teachers
        mock_conn.return_value.cursor.return_value = mock_cursor

        self.view.display()

        tree_items = self.view.tree.get_children()
        for i, teacher in enumerate(teachers):
            item_values = self.view.tree.item(tree_items[i])['values']
            self.assertEqual(list(item_values), list(teacher))

        # Assert that the UI elements are initialized correctly

        # Check the existence of UI elements
        self.assertIsInstance(self.view.tree, ttk.Treeview)
        self.assertIsInstance(self.view.add_button, ttk.Button)
        self.assertIsInstance(self.view.delete_button, ttk.Button)
        self.assertIsInstance(self.view.back_button, ttk.Button)

        # Check the initial state of UI elements
        self.assertEqual(str(self.view.delete_button["state"]), "disabled")

    def test_on_tree_select(self):
        # Test the on_tree_select method when an item is selected in the treeview
        # Assert that the delete button state is enabled

        # Select an item in the treeview
        selected_item = self.view.tree.get_children()[0]  # Select the first item
        self.view.tree.selection_set(selected_item)

        # Call the on_tree_select method
        self.view.on_tree_select(Mock())

        # Assert that the delete button state is enabled
        self.assertEqual(str(self.view.delete_button["state"]), "enabled")

    def test_on_tree_select_no_selection(self):
        # Test the on_tree_select method when no item is selected in the treeview
        # Assert that the delete button state is disabled

        # Clear the selection in the treeview
        self.view.tree.selection_set()

        # Call the on_tree_select method
        self.view.on_tree_select(Mock())

        # Assert that the delete button state is disabled
        self.assertEqual(str(self.view.delete_button["state"]), "disabled")

    def test_add_teacher(self):
        # Test the add_discipline method
        # Assert that the master's switch_frame method is called with AddTeacherForm

        # Create a mock master
        mock_master = Mock()

        # Set the view's master to the mock master
        self.view.master = mock_master

        # Call the add_discipline method
        self.view.add_discipline()

        # Assert that the master's switch_frame method is called with AddTeacherForm
        mock_master.switch_frame.assert_called_with(AddTeacherForm)

    def test_go_back(self):
        # Test the go_back method
        # Assert that the master's switch_frame method is called with AdminPage

        # Create a mock master
        mock_master = Mock()

        # Set the view's master to the mock master
        self.view.master = mock_master

        # Call the go_back method
        self.view.go_back()

        # Assert that the master's switch_frame method is called with AdminPage
        mock_master.switch_frame.assert_called_with(admin.AdminPage)

