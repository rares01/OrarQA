import unittest
from unittest.mock import patch, Mock
import tkinter as tk
from tkinter import ttk
import ui.admin.views.disciplines_view as disciplines_view_module
from entities.discipline import Discipline
from repositories.discipline_repo import get_disciplines, get_discipline_id_by_value, delete_discipline
from ui.admin.forms.disciplines.add_discipline import AddDisciplineForm


class TestDisciplinesView(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up any required test data or dependencies for the entire test class
        cls.root = tk.Tk()

    def setUp(self):
        # Set up any required test data or dependencies for each individual test case
        self.view = disciplines_view_module.DisciplinesView(self.root)

    def test_display(self):
        # Test the display method to ensure the UI is set up correctly
        # Assert that the UI elements are initialized correctly

        # Test the display method to populate the treeview with disciplines

        # Set up the expected disciplines
        expected_disciplines = [
            (10, "TW", 1, "Jane Smith"),
            (11, "BD", 1, "Jane Smith"),
            (12, "SD", 1, "Jane Smith")
        ]

        get_disciplines = Mock(
            return_value=[Mock(id=id, name=name, study_year_id=study_year_id, teacher_name=teacher_name)
                          for id, name, study_year_id, teacher_name in expected_disciplines])

        # Patch the get_disciplines function to return the expected disciplines
        with patch("repositories.discipline_repo.get_disciplines", get_disciplines):
            self.view.display()

            # Assert that the treeview is populated with the disciplines
            tree_items = self.view.tree.get_children()
            for i, discipline in enumerate(expected_disciplines):
                item_values = self.view.tree.item(tree_items[i])['values']
                self.assertEqual(list(item_values), list(discipline[0:4]))

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

    def test_apply_filters(self):
        # Test the apply_filters method to filter disciplines based on study year and teacher
        # Assert that the treeview is updated with the filtered disciplines

        # Set the initial disciplines to the mock disciplines
        self.view.disciplines = get_disciplines()
        for discipline in self.view.disciplines:
            self.view.tree.insert("", "end", values=(
                discipline.id, discipline.name, discipline.study_year, discipline.teacher_full_name))
        # Apply the filters to select study year 1 and teacher "John Doe"
        self.view.study_year_filter.current(1)
        self.view.teachers_filter.current(1)
        self.view.apply_filters()

        # Assert that the treeview is updated with the filtered disciplines
        self.assertEqual(len(self.view.tree.get_children()), 8)
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

    def test_delete_discipline(self):
        # Test the delete_discipline method to delete a selected discipline
        # Assert that the discipline is deleted and the treeview is updated

        self.view.disciplines = get_disciplines()

        # Select the second discipline in the treeview
        self.view.tree.selection_set(self.view.tree.get_children()[0])

        # Call the delete_discipline method
        disciplines_number = len(self.view.tree.get_children())
        self.view.delete_discipline()

        # Assert that the delete_discipline method is called with the correct discipline ID
        # delete_discipline.assert_called_once_with(2)

        # Assert that the treeview is updated after the deletion
        self.assertEqual(len(self.view.tree.get_children()), disciplines_number-1)
        expected_updated_disciplines = [
            self.view.disciplines[1],
            self.view.disciplines[2],
            self.view.disciplines[3]
        ]
        for i, discipline in enumerate(expected_updated_disciplines):
            item_values = self.view.tree.item(self.view.tree.get_children()[i])["values"]
            self.assertEqual(item_values[0], discipline.id)
            self.assertEqual(item_values[1], discipline.name)
            self.assertEqual(item_values[2], discipline.study_year)
            self.assertEqual(item_values[3], discipline.teacher_full_name)
