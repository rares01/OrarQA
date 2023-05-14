import unittest
from tkinter import ttk
import tkinter as tk
from unittest.mock import Mock, patch
import ui.admin.admin_page as admin

from ui.admin.views.timetable_view import TimetableView


class TestTimetableView(unittest.TestCase):
    def setUp(self):
        root = tk.Tk()
        self.view = TimetableView(root)

    # todo: Andrei Mosor
    # revise this whole class, implementation not clear, also missing data from DB, possibly missing commit

    def test_display(self):
        # Test the display method to ensure the UI is set up correctly
        # Assert that the treeview is populated with the correct data

        # Create a mock timetable entry list

        timetable_entries = [
            (1, "Monday", "9:00 AM", "John Doe", "SD", 2023, "Spring", 1),
            (2, "Tuesday", "2:00 PM", "Jane Smith", "English", 2022, "Fall", 2),
            (3, "Wednesday", "11:00 AM", "John Doe", "Physics", 2023, "Spring", 1)
        ]

        # Mock the get_entries function to return the mock timetable entry list
        get_entries = Mock(
            return_value=timetable_entries
        )

        # Set the get_entries function as the target function for patching
        with patch("repositories.scheduler_entry_repo.get_entries", get_entries):
            # Call the display method
            self.view.display()

            # todo: there is no data in database, scheduler missing
            # Assert that the treeview is populated with the correct data
            tree_items = self.view.tree.get_children()
            for i, entry in enumerate(timetable_entries):
                item_values = self.view.tree.item(tree_items[i])['values']
                self.assertEqual(list(item_values), list(entry[0:6]))

        # Assert that the UI elements are initialized correctly

        # Check the existence of UI elements
        self.assertIsInstance(self.view.tree, ttk.Treeview)
        self.assertIsInstance(self.view.add_button, ttk.Button)
        self.assertIsInstance(self.view.delete_button, ttk.Button)
        self.assertIsInstance(self.view.back_button, ttk.Button)
        self.assertIsInstance(self.view.generate_html, ttk.Button)
        self.assertIsInstance(self.view.weekday_filter, ttk.Combobox)
        self.assertIsInstance(self.view.time_slot_filter, ttk.Combobox)
        self.assertIsInstance(self.view.teacher_filter, ttk.Combobox)
        self.assertIsInstance(self.view.discipline_filter, ttk.Combobox)
        self.assertIsInstance(self.view.study_year_filter, ttk.Combobox)
        self.assertIsInstance(self.view.semi_year_filter, ttk.Combobox)
        self.assertIsInstance(self.view.group_filter, ttk.Combobox)

        # Check the initial state of UI elements
        self.assertEqual(str(self.view.delete_button["state"]), "disabled")

    def test_go_back(self):
        # Test the on_back_button_click method when the back button is clicked
        # Assert that the root window is destroyed

        # Create a mock root window
        self.view.master.switch_frame = Mock()

        # Call the on_back_button_click method
        self.view.go_back()

        # Assert that the root window is destroyed
        self.view.master.switch_frame.assert_called_with(admin.AdminPage)

    def test_on_generate_html_button_click(self):
        # Test the on_generate_html_button_click method when the generate HTML button is clicked
        # Assert that the generate_html method is called

        # Create a mock generator
        mock_generator = Mock()

        # todo: Rares Gramescu
        # todo: improve this, method is outside of TimetableView class

        # Set the mock generator as the target function for patching
        with patch("generator.generate_html", mock_generator):
            # Call the on_generate_html_button_click method
            self.view.go_to_html(Mock())

            # Assert that the generate_html method is called
            mock_generator.assert_called_once()

