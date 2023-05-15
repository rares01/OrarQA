import unittest
from unittest.mock import patch, Mock, MagicMock
import tkinter as tk
from tkinter import ttk
import ui.admin.views.disciplines_view as disciplines_view_module
import ui.admin.admin_page as admin
from entities.discipline import Discipline
from repositories.discipline_repo import get_disciplines, get_discipline_id_by_value, delete_discipline
from ui.admin.forms.disciplines.add_discipline import AddDisciplineForm


def side_effect(id):
    if id == 1:
        return "Jane Smith"
    else:
        return "John Smith"


class TestDisciplinesView(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up any required test data or dependencies for the entire test class
        cls.root = tk.Tk()

    def setUp(self):
        # Set up any required test data or dependencies for each individual test case
        self.view = disciplines_view_module.DisciplinesView(self.root)

    @patch('repositories.discipline_repo.connection')
    @patch('repositories.teacher_repo.get_teacher_full_name_by_id')
    def test_display(self, mock_teacher_full_name_by_id, mock_conn_disciplines):

        expected_disciplines = [
            (10, "TW", 1, 1),
            (11, "BD", 1, 1),
            (12, "SD", 1, 1)
        ]

        mock_cursor_disciplines = MagicMock()
        mock_cursor_disciplines.fetchall.return_value = expected_disciplines
        mock_conn_disciplines.return_value.cursor.return_value = mock_cursor_disciplines

        mock_teacher_full_name_by_id.side_effect = side_effect
        self.view.display()

        tree_items = self.view.tree.get_children()
        for i, discipline in enumerate(get_disciplines()):
            item_values = self.view.tree.item(tree_items[i])['values']
            self.assertEqual(item_values[0], discipline.id)
            self.assertEqual(item_values[1], discipline.name)
            self.assertEqual(item_values[2], discipline.study_year)

        # Check the existence of UI elements
        self.assertIsInstance(self.view.tree, ttk.Treeview)
        self.assertIsInstance(self.view.add_button, ttk.Button)
        self.assertIsInstance(self.view.delete_button, ttk.Button)
        self.assertIsInstance(self.view.back_button, ttk.Button)
        self.assertIsInstance(self.view.study_year_filter, ttk.Combobox)
        self.assertIsInstance(self.view.teachers_filter, ttk.Combobox)

        # Check the initial state of UI elements
        self.assertEqual(len(self.view.tree.get_children()), len(disciplines_view_module.get_disciplines()))
        self.assertEqual(str(self.view.delete_button["state"]), "disabled")
        self.assertEqual(self.view.study_year_filter.get(), "All")
        self.assertEqual(self.view.teachers_filter.get(), "All")

    def test_on_tree_select(self):
        # Test the on_tree_select method when an item is selected in the treeview
        # Assert that the delete button state is enabled

        selected_item = self.view.tree.get_children()[0]  # Select the first item in the treeview
        self.view.tree.selection_set(selected_item)

        # Call the on_tree_select method
        self.view.on_tree_select(Mock())

        # Assert that the delete button state is enabled
        self.assertEqual(str(self.view.delete_button["state"]), "enabled")

    def test_on_tree_select_no_selection(self):
        # Test the on_tree_select method when no item is selected in the treeview
        # Assert that the delete button state is disabled

        # Clear the selection in the treeview
        self.view.tree.selection_clear()

        # Call the on_tree_select method
        self.view.on_tree_select(Mock())

        # Assert that the delete button state is disabled
        self.assertEqual(str(self.view.delete_button["state"]), "disabled")

    @patch('repositories.discipline_repo.connection')
    @patch('repositories.teacher_repo.get_teacher_full_name_by_id')
    def test_apply_filters(self, mock_teacher_full_name_by_id, mock_conn_disciplines):
        expected_disciplines = [
            (10, "TW", 1, 1),
            (11, "BD", 1, 1),
            (12, "SD", 1, 1)
        ]

        mock_cursor_disciplines = MagicMock()
        mock_cursor_disciplines.fetchall.return_value = expected_disciplines
        mock_conn_disciplines.return_value.cursor.return_value = mock_cursor_disciplines

        mock_teacher_full_name_by_id.side_effect = side_effect

        self.view.disciplines = get_disciplines()
        for discipline in self.view.disciplines:
            self.view.tree.insert("", "end", values=(
                discipline.id, discipline.name, discipline.study_year, discipline.teacher_full_name))
        self.view.study_year_filter.current(1)
        self.view.teachers_filter.current(1)
        self.view.apply_filters()

        # Assert that the treeview is updated with the filtered disciplines
        self.assertEqual(len(self.view.tree.get_children()), len(expected_disciplines))
        expected_filtered_disciplines = [
            self.view.disciplines[0],
            self.view.disciplines[1]
        ]
        for i, discipline in enumerate(expected_filtered_disciplines):
            item_values = self.view.tree.item(self.view.tree.get_children()[i])["values"]
            self.assertEqual(item_values[0], discipline.id)
            self.assertEqual(item_values[1], discipline.name)
            self.assertEqual(item_values[2], discipline.study_year)
            self.assertEqual(item_values[3], discipline.teacher_full_name)

    def test_add_discipline(self):
        # Test the add_discipline method to add a new discipline to the treeview

        # Mock the switch_frame method
        self.view.master.switch_frame = Mock()

        # Call the add_discipline method
        self.view.add_discipline()

        # Assert that the frame is switched correctly
        self.view.master.switch_frame.assert_called_with(AddDisciplineForm)

    @patch('repositories.discipline_repo.connection')
    @patch('repositories.teacher_repo.get_teacher_full_name_by_id')
    def test_delete_discipline(self, mock_teacher_full_name, mock_conn_disciplines):

        expected_disciplines = [
            (Discipline(10, "TW", 1, 'Jane Smith'),),
            (Discipline(11, "BD", 1, 'Jane Smith'),),
            (Discipline(12, "SD", 1, 'Jane Smith'),)
        ]

        mock_cursor_disciplines = MagicMock()
        mock_conn_disciplines.return_value.cursor.return_value = mock_cursor_disciplines
        self.view.disciplines = get_disciplines()
        mock_teacher_full_name.side_effect = side_effect

        self.view.tree.selection_set(self.view.tree.get_children()[0])

        # Call the delete_discipline method

        self.view.delete_discipline()

        # Assert that the delete_discipline method is called with the correct discipline ID
        # delete_discipline.assert_called_once_with(2)

        # Assert that the treeview is updated after the deletion
        self.assertEqual(len(self.view.tree.get_children()), 0)

        expected_updated_disciplines = [
            expected_disciplines[1],
            expected_disciplines[2]
        ]

        disciplines = []
        for discipline in expected_updated_disciplines:
            disciplines.append(Discipline(discipline[0].id, discipline[0].name, discipline[0].study_year,
                                          discipline[0].teacher_full_name))

        self.view.update_treeview(disciplines)
        for i, discipline in enumerate(expected_updated_disciplines):
            item_values = self.view.tree.item(self.view.tree.get_children()[i])["values"]
            self.assertEqual(item_values[0], discipline[0].id)
            self.assertEqual(item_values[1], discipline[0].name)
            self.assertEqual(item_values[2], discipline[0].study_year)
            self.assertEqual(item_values[3], discipline[0].teacher_full_name)

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
