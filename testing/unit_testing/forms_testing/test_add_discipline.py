import unittest
import tkinter as tk
from tkinter import ttk
from unittest.mock import Mock

from ui.admin.views import disciplines_view
from repositories.discipline_repo import add_discipline, get_disciplines
from repositories.study_year_repo import get_study_years_values
from repositories.teacher_repo import get_teacher_full_names
from ui.admin.forms.disciplines.add_discipline import AddDisciplineForm
from ui.admin.views.disciplines_view import DisciplinesView


class TestAddDisciplineForm(unittest.TestCase):
    def setUp(self):
        # Create a root window for testing
        self.root = tk.Tk()

    def test_handle(self):
        # Test the handle method to add a discipline
        # Assert that the discipline is added correctly

        # Create an instance of AddDisciplineForm
        form = AddDisciplineForm(self.root)
        view = DisciplinesView(self.root)

        # Set up the test data
        name = "Math"
        year = 1
        teacher = "John Doe"

        # Call the handle method
        form.handle(name_entry=tk.StringVar(value=name), year_entry=tk.StringVar(value=str(year)),
                    teacher_entry=tk.StringVar(value=teacher))

        # Get the list of disciplines
        disciplines = get_disciplines()

        # Assert that the discipline is added correctly
        self.assertEqual(len(disciplines), len(view.disciplines) + 1)
        self.assertEqual(disciplines[len(disciplines)-1].name, name)
        self.assertEqual(disciplines[len(disciplines)-1].study_year, year)
        self.assertEqual(disciplines[len(disciplines)-1].teacher_full_name, teacher)

    # todo: improve, does not work
    def test_go_back(self):
        # Test the go_back method to navigate back to the disciplines view
        # Assert that the disciplines view is displayed and the disciplines are updated

        # Create an instance of AddDisciplineForm
        form = AddDisciplineForm(self.root)

        # Create a mock master
        mock_master = Mock()

        # Set the view's master to the mock master
        form.master = mock_master

        # Set up the test data
        disciplines = [{"name": "Math", "year": "1", "teacher": "John Doe"}]
        form.disciplines_view = disciplines_view.DisciplinesView(self.root)
        form.disciplines_view.set_disciplines(disciplines)

        # Call the go_back method
        form.go_back()

        # Get the current frame
        current_frame = self.root.winfo_children()[-1]

        # Assert that the current frame is the disciplines view
        self.assertIsInstance(current_frame, disciplines_view.DisciplinesView)

        # Assert that the disciplines are updated in the view
        updated_disciplines = form.disciplines_view.disciplines
        self.assertEqual(len(updated_disciplines), 1)
        self.assertEqual(updated_disciplines[0]["name"], disciplines[0]["name"])
        self.assertEqual(updated_disciplines[0]["year"], disciplines[0]["year"])
        self.assertEqual(updated_disciplines[0]["teacher"], disciplines[0]["teacher"])
