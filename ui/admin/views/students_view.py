import tkinter as tk
from tkinter import ttk

import ui.admin.admin_page as admin
from entities.student import Student
from repositories.semi_year_repo import get_semi_years_values
from repositories.student_group_repo import get_student_groups_values
from repositories.student_repo import get_students, delete_student
from repositories.study_year_repo import get_study_years_values
from ui.admin.forms.students.add_students import AddStudentForm


class StudentsView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.semi_year_filter = None
        self.group_filter = None
        self.study_year_filter = None
        self.students = None
        self.back_button = None
        self.tree = None
        self.add_button = None
        self.delete_button = None
        self.master = master
        self.display()

    def display(self):
        assert callable(get_students), "get_students must be a callable function."

        self.students = get_students()

        title_label = ttk.Label(self, text="Students View", font=("Helvetica", 20))
        title_label.pack(pady=20)

        self.tree = ttk.Treeview(self, columns=("ID", "First Name", "Last Name", "Study Year", "Semi Year", "Student "
                                                                                                            "Group"),
                                 show="headings")
        self.tree.column('ID', width=50)
        self.tree.column('First Name', width=50)
        self.tree.column('Last Name', width=50)
        self.tree.column('Study Year', width=50)
        self.tree.column('Semi Year', width=50)
        self.tree.column('Student Group', width=50)
        self.tree.pack(padx=10, pady=10, fill="both", expand=True)

        for col in ("ID", "First Name", "Last Name", "Study Year", "Semi Year", "Student Group"):
            self.tree.heading(col, text=col, anchor="center")

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Helvetica", 16))
        style.configure("Treeview", font=("Helvetica", 12))

        for student in self.students:
            self.tree.insert("", "end", values=(
                student.id, student.first_name, student.last_name, student.study_year, student.semi_year,
                student.student_group))

        self.add_button = ttk.Button(self, text="Add", command=self.add_student, style="Custom.TButton")
        self.add_button.pack(side="top", pady=10)

        self.delete_button = ttk.Button(self, text="Delete", command=self.delete_student, state="disabled",
                                        style="Custom.TButton")
        self.delete_button.pack(side="left", padx=10, pady=10)

        self.back_button = ttk.Button(self, text="Back", command=self.go_back, style="Custom.TButton")
        self.back_button.pack(side="right", padx=10, pady=10)

        self.tree.bind("<ButtonRelease-1>", self.on_tree_select)

        style.configure("Custom.TButton", font=("Helvetica", 12), background="#d8d8d8", foreground="#333",
                        borderwidth=0, focuscolor="#d8d8d8", lightcolor="#d8d8d8", darkcolor="#d8d8d8")

        year_filter_label = ttk.Label(self, text="Filter by Year:", font=("Helvetica", 14))
        year_filter_label.pack(side="left")
        study_year_ids = get_study_years_values()
        study_year_ids.insert(0, "All")
        self.study_year_filter = ttk.Combobox(self, values=study_year_ids, state="readonly")
        self.study_year_filter.bind("<<ComboboxSelected>>", lambda event: self.apply_filters())
        self.study_year_filter.current(0)
        self.study_year_filter.pack(side="left", padx=5)

        semi_year_filter_label = ttk.Label(self, text="Filter by Semi Year:", font=("Helvetica", 14))
        semi_year_filter_label.pack(side="left")
        semi_year_ids = get_semi_years_values()
        semi_year_ids.insert(0, "All")
        self.semi_year_filter = ttk.Combobox(self, values=semi_year_ids, state="readonly")
        self.semi_year_filter.bind("<<ComboboxSelected>>", lambda event: self.apply_filters())
        self.semi_year_filter.current(0)
        self.semi_year_filter.pack(side="left", padx=5)

        group_filter_label = ttk.Label(self, text="Filter by Group:", font=("Helvetica", 14))
        group_filter_label.pack(side="left")
        group_ids = get_student_groups_values()
        group_ids.insert(0, "All")
        self.group_filter = ttk.Combobox(self, values=group_ids, state="readonly")
        self.group_filter.bind("<<ComboboxSelected>>", lambda event: self.apply_filters())
        self.group_filter.current(0)
        self.group_filter.pack(side="left", padx=5)

        assert isinstance(self.tree, ttk.Treeview), "self.tree must be a valid ttk.Treeview object."
        assert isinstance(self.add_button, ttk.Button), "self.add_button must be a valid ttk.Button object."
        assert isinstance(self.delete_button, ttk.Button), "self.delete_button must be a valid ttk.Button object."
        assert isinstance(self.back_button, ttk.Button), "self.back_button must be a valid ttk.Button object."
        assert callable(self.add_student), "self.add_student must be a callable function."
        assert callable(self.delete_student), "self.delete_student must be a callable function."
        assert callable(self.go_back), "self.go_back must be a callable function."
        assert isinstance(self.study_year_filter,
                          ttk.Combobox), "self.study_year_filter must be a valid ttk.Combobox object."
        assert isinstance(self.semi_year_filter,
                          ttk.Combobox), "self.semi_year_filter must be a valid ttk.Combobox object."
        assert isinstance(self.group_filter, ttk.Combobox), "self.group_filter must be a valid ttk.Combobox object."

    def set_students(self, current_students):
        assert isinstance(current_students, list), "current_students should be a list"

        self.students = current_students

        assert self.students == current_students, "self.students should be set to the current students"

    def on_tree_select(self, event):
        assert isinstance(self.tree, ttk.Treeview), "self.tree must be a valid ttk.Treeview object."
        assert isinstance(self.delete_button, ttk.Button), "self.delete_button must be a valid ttk.Button object."

        selection = self.tree.selection()
        if selection:
            self.delete_button.config(state="enabled")
        else:
            self.delete_button.config(state="disabled")

        assert isinstance(self.delete_button, ttk.Button), "self.delete_button must be a valid ttk.Button object."

    def apply_filters(self):
        assert isinstance(self.study_year_filter,
                          ttk.Combobox), "self.study_year_filter must be a valid ttk.Combobox object."
        assert isinstance(self.semi_year_filter,
                          ttk.Combobox), "self.semi_year_filter must be a valid ttk.Combobox object."
        assert isinstance(self.group_filter, ttk.Combobox), "self.group_filter must be a valid ttk.Combobox object."

        year = self.study_year_filter.get()
        semi_year = self.semi_year_filter.get()
        group = self.group_filter.get()

        filtered_students = []

        for student in self.students:
            if year != "All" and student.study_year != int(year):
                continue
            if group != "All" and student.student_group != int(group):
                continue
            if semi_year != "All" and student.semi_year != semi_year:
                continue

            filtered_students.append(student)

        self.update_treeview(filtered_students)

        assert isinstance(filtered_students, list), "filtered_students must be a list."
        assert all(isinstance(student, Student) for student in
                   filtered_students), "All items in filtered_students must be instances of Student class."

    def update_treeview(self, filtered_students):
        assert isinstance(self.tree, ttk.Treeview), "self.tree should be an instance of ttk.Treeview"
        assert isinstance(filtered_students, list), "filtered_students should be a list"

        self.tree.delete(*self.tree.get_children())
        for student in filtered_students:
            self.tree.insert("", "end", values=(
                student.id, student.first_name, student.last_name, student.study_year, student.semi_year,
                student.student_group))

        children = self.tree.get_children()
        assert len(children) == len(
            filtered_students), "Number of treeview items should match the number of filtered disciplines"

        for i, student in enumerate(filtered_students):
            item_values = self.tree.item(children[i])["values"]
            assert item_values == (student.id, student.first_name, student.study_year,
                                   student.semi_year, student.student_group), "Mismatch in treeview item values"

    def add_student(self):
        assert hasattr(self.master, "switch_frame"), "self.master should have the 'switch_frame' method"

        self.master.switch_frame(AddStudentForm)

        assert self.master.current_frame == AddStudentForm, "Expected current_frame to be set to AddStudentForm"

    def go_back(self):
        assert hasattr(self.master, "switch_frame"), "self.master should have the 'switch_frame' method"

        self.master.switch_frame(admin.AdminPage)

        assert self.master.current_frame == admin.AdminPage, "Expected current_frame to be set to AdminPage"

    def delete_student(self):
        selection = self.tree.selection()
        if selection:
            values = self.tree.item(selection)["values"]
            delete_student(values[0])
            assert all(student.id is not values[0] for student in get_students())
        self.update_treeview(get_students())
