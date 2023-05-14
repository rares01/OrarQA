import unittest
from tkinter import ttk
from unittest.mock import Mock, patch
import tkinter as tk
import ui.admin.views.students_view as students_view_module
import ui.admin.admin_page as admin
from entities.discipline import Discipline
from entities.student import Student
from ui.admin.forms.students.add_students import AddStudentForm


class TestStudentsView(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up any required test data or dependencies for the entire test class
        cls.root = tk.Tk()

    def setUp(self):
        # Set up any required test data or dependencies for each individual test case
        self.view = students_view_module.StudentsView(self.root)

    def test_display(self):
        # Test the display method to ensure the UI is set up correctly
        # Assert that the UI elements are initialized correctly

        # Create a mock student list
        students = [
            (5, "Alice", "Smith", 1, "A", 101),
            (6, "Bob", "Jones", 1, "A", 101),
            (7, "Adrian", "Smau", 1, "A", 102),
            (8, "Rares", "Gramescu", 1, "A", 102)
        ]

        # Mock the get_students function to return the mock student list
        get_students_mock = Mock(return_value=[
            Mock(id=id, first_name=first_name, last_name=last_name, study_year=study_year, semi_year=semi_year,
                 discipline=discipline)
            for id, first_name, last_name, study_year, semi_year, discipline in students
        ])

        # Mock the get_groups function to return an empty list
        get_groups_mock = Mock(return_value=[])

        # Mock the get_full_teachers function to return an empty list
        get_full_teachers_mock = Mock(return_value=[])

        # Patch the repository functions with the mock functions
        with patch("repositories.student_repo.get_students", get_students_mock), \
             patch("repositories.student_group_repo.get_student_groups_values", get_groups_mock), \
             patch("repositories.teacher_repo.get_full_teachers", get_full_teachers_mock):
            # Call the display method
            self.view.display()

            # Assert that the treeview is populated with the correct data
            tree_items = self.view.tree.get_children()
            for i, student in enumerate(students):
                item_values = self.view.tree.item(tree_items[i])['values']
                self.assertEqual(list(item_values), list(student[0:6]))

        # Check the existence of UI elements
        self.assertIsInstance(self.view.tree, ttk.Treeview)
        self.assertIsInstance(self.view.add_button, ttk.Button)
        self.assertIsInstance(self.view.delete_button, ttk.Button)
        self.assertIsInstance(self.view.back_button, ttk.Button)
        self.assertIsInstance(self.view.semi_year_filter, ttk.Combobox)
        self.assertIsInstance(self.view.group_filter, ttk.Combobox)
        self.assertIsInstance(self.view.study_year_filter, ttk.Combobox)

        # Check the initial state of UI elements
        self.assertEqual(len(self.view.tree.get_children()), len(students_view_module.get_students()))
        self.assertEqual(str(self.view.delete_button["state"]), "disabled")
        self.assertEqual(self.view.semi_year_filter.get(), "All")
        self.assertEqual(self.view.group_filter.get(), "All")
        self.assertEqual(self.view.study_year_filter.get(), "All")

    def test_on_tree_select(self):
        # Test the on_tree_select method when an item is selected in the treeview
        # Assert that the delete button state is enabled

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
        self.view.tree.selection_clear()

        # Call the on_tree_select method
        self.view.on_tree_select(Mock())

        # Assert that the delete button state is disabled
        self.assertEqual(str(self.view.delete_button["state"]), "disabled")

    def test_apply_filters(self):
        # Test the apply_filters method to filter the students based on the selected filters
        # Assert that the treeview is updated with the filtered students

        # Set up the initial state of the treeview
        self.view.students = students_view_module.get_students()
        for student in self.view.students:
            self.view.tree.insert("", "end", values=(
                student.id, student.first_name, student.last_name, student.study_year, student.semi_year,
                student.student_group))

        # Apply the filters
        self.view.study_year_filter.set("1")
        self.view.semi_year_filter.set("A")
        self.view.group_filter.set("All")
        self.view.apply_filters()

        # Set the expected filtered students
        expected_filtered_students = [
            self.view.students[0],
            self.view.students[1]
        ]

        # Assert that the treeview is updated with the filtered students
        self.assertEqual(len(self.view.tree.get_children()), 6)
        for i, student in enumerate(expected_filtered_students):
            values = self.view.tree.item(self.view.tree.get_children()[i])['values']
            self.assertEqual(values[0], student.id)
            self.assertEqual(values[1], student.first_name)
            self.assertEqual(values[2], student.last_name)
            self.assertEqual(values[3], student.study_year)
            self.assertEqual(values[4], student.semi_year)
            self.assertEqual(values[5], student.student_group)

    def test_update_treeview(self):
        # Test the update_treeview method to update the treeview with the provided students
        # Assert that the treeview is updated correctly

        # Clear the treeview
        self.view.tree.delete(*self.view.tree.get_children())

        # Set the students to be inserted into the treeview
        students = [
            Student(1, "John", "Doe", 1, "First", "Group A"),
            Student(2, "Jane", "Smith", 2, "Second", "Group B")
        ]

        # Update the treeview with the students
        self.view.update_treeview(students)

        # Assert that the treeview is updated correctly
        self.assertEqual(len(self.view.tree.get_children()), len(students))
        for i, student in enumerate(students):
            values = self.view.tree.item(self.view.tree.get_children()[i])['values']
            self.assertEqual(values[0], student.id)
            self.assertEqual(values[1], student.first_name)
            self.assertEqual(values[2], student.last_name)
            self.assertEqual(values[3], student.study_year)
            self.assertEqual(values[4], student.semi_year)
            self.assertEqual(values[5], student.student_group)

    def test_add_student(self):
        # Test the add_student method to switch the frame to the AddStudentForm
        # Assert that the frame is switched correctly

        # Mock the switch_frame method
        self.view.master.switch_frame = Mock()

        # Call the add_student method
        self.view.add_student()

        # Assert that the frame is switched correctly
        self.view.master.switch_frame.assert_called_with(AddStudentForm)

    def test_go_back(self):
        # Test the go_back method to switch the frame to the AdminPage
        # Assert that the frame is switched correctly

        # Mock the switch_frame method
        self.view.master.switch_frame = Mock()

        # Call the go_back method
        self.view.go_back()

        # Assert that the frame is switched correctly
        self.view.master.switch_frame.assert_called_with(admin.AdminPage)

    def test_delete_student(self):
        # Test the delete_student method to delete a student from the database and update the treeview
        # Assert that the student is deleted and the treeview is updated correctly

        # Set up the initial state of the treeview
        self.view.students = students_view_module.get_students()

        # Select the first student in the treeview
        # Select the first student in the treeview
        self.view.tree.selection_set(self.view.tree.get_children()[0])

        # Call the delete_student method
        self.view.delete_student()

        # Assert that the student is deleted and the treeview is updated correctly
        # students_view_module.delete_student.assert_called_with(self.view.students[0].id)
        self.assertEqual(len(self.view.tree.get_children()), len(self.view.students) - 1)

        # todo: update when connection mock works, so that assert_not_called function can work.

        # # Select a student that is not in the treeview
        # self.view.tree.selection_set("invalid_id")
        #
        # # Call the delete_student method
        # self.view.delete_student()
        #
        # # Assert that the delete_student function is not called and the treeview remains the same
        # # students_view_module.delete_student.assert_not_called()
        # self.assertEqual(len(self.view.tree.get_children()), len(self.view.students) - 1)

    def test_set_students(self):
        # Test the set_students method to update the students in the view
        # Assert that the students are updated correctly

        # Set the students
        students = [
            Student(1, "John", "Doe", 1, "First", "Group A"),
            Student(2, "Jane", "Smith", 2, "Second", "Group B")
        ]
        self.view.set_students(students)

        # Assert that the students are updated correctly
        self.assertEqual(self.view.students, students)

