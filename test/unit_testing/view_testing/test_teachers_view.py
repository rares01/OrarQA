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

        teachers = [
            (1, "Jane", "Smith"),
            (2, "John", "Doe"),
            (3, "Jane", "Smith"),
            (4, "John", "Doe")
        ]

        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = teachers
        mock_conn.return_value.cursor.return_value = mock_cursor
        mock_conn.return_value.closed = 1

        self.view.display()

        tree_items = self.view.tree.get_children()
        for i, teacher in enumerate(teachers):
            item_values = self.view.tree.item(tree_items[i])['values']
            self.assertEqual(list(item_values), list(teacher))

        self.assertIsInstance(self.view.tree, ttk.Treeview)
        self.assertIsInstance(self.view.add_button, ttk.Button)
        self.assertIsInstance(self.view.delete_button, ttk.Button)
        self.assertIsInstance(self.view.back_button, ttk.Button)

        self.assertEqual(str(self.view.delete_button["state"]), "disabled")

    def test_on_tree_select(self):
        selected_item = self.view.tree.get_children()[0]
        self.view.tree.selection_set(selected_item)

        self.view.on_tree_select(Mock())

        self.assertEqual(str(self.view.delete_button["state"]), "enabled")

    def test_on_tree_select_no_selection(self):
        self.view.tree.selection_set()

        self.view.on_tree_select(Mock())

        self.assertEqual(str(self.view.delete_button["state"]), "disabled")

    def test_add_teacher(self):
        mock_master = Mock()

        self.view.master = mock_master

        self.view.add_discipline()

        mock_master.switch_frame.assert_called_with(AddTeacherForm)

    def test_go_back(self):
        mock_master = Mock()

        self.view.master = mock_master

        self.view.go_back()

        mock_master.switch_frame.assert_called_with(admin.AdminPage)

