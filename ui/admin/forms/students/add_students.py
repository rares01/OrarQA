import tkinter as tk
from tkinter import ttk

import ui.admin.views.students_view as view
from repositories.semi_year_repo import get_semi_years_values
from repositories.student_group_repo import get_student_groups_values
from repositories.student_repo import add_student, get_students
from repositories.study_year_repo import get_study_years_values


def handle(first_name_entry=None, last_name_entry=None, study_year_var=None, semi_year_var=None,
           student_group_var=None):
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    study_year = study_year_var.get()
    semi_year = semi_year_var.get()
    student_group = student_group_var.get()
    add_student(first_name=first_name, last_name=last_name, study_year=study_year, semi_year=semi_year,
                student_group=student_group)


class AddStudentForm(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.back_button = None
        for child in master.winfo_children():
            if isinstance(child, view.StudentsView):
                self.students_view = child
                break
        self.display()

    def display(self):
        title_label = ttk.Label(self, text="Add Student Form", font=("Helvetica", 20))
        title_label.pack(pady=20)
        style = ttk.Style()
        style.configure('TLabel', font=('Helvetica', 14), padding=10)
        style.configure('TEntry', font=('Helvetica', 14), padding=10)
        style.configure('TCombobox', font=('Helvetica', 14), padding=10)
        style.configure('TButton', font=('Helvetica', 14), padding=10)
        first_name_label = ttk.Label(self, text="First Name:")
        last_name_label = ttk.Label(self, text="Last Name:")
        study_year_label = ttk.Label(self, text="Study Year:")
        semi_year_label = ttk.Label(self, text="Semi Year:")
        student_group_label = ttk.Label(self, text="Student Group:")
        first_name_entry = ttk.Entry(self)
        last_name_entry = ttk.Entry(self)
        study_year_ids = get_study_years_values()
        study_year_var = tk.StringVar(self)
        study_year_var.set(study_year_ids[0])
        study_year_dropdown = ttk.Combobox(self, textvariable=study_year_var, values=study_year_ids, state='readonly')
        semi_year_ids = get_semi_years_values()
        semi_year_var = tk.StringVar(self)
        semi_year_var.set(semi_year_ids[0])
        semi_year_dropdown = ttk.Combobox(self, textvariable=semi_year_var, values=semi_year_ids, state='readonly')
        student_group_ids = get_student_groups_values()
        student_group_var = tk.StringVar(self)
        student_group_var.set(student_group_ids[0])
        student_group_dropdown = ttk.Combobox(self, textvariable=student_group_var, values=student_group_ids,
                                              state='readonly')
        first_name_label.pack()
        first_name_entry.pack()
        last_name_label.pack()
        last_name_entry.pack()
        study_year_label.pack()
        study_year_dropdown.pack()
        semi_year_label.pack()
        semi_year_dropdown.pack()
        student_group_label.pack()
        student_group_dropdown.pack()
        add_student_button = ttk.Button(self, text="Add",
                                        command=lambda: handle(first_name_entry, last_name_entry, study_year_var,
                                                               semi_year_var, student_group_var))
        add_student_button.pack()

        self.back_button = ttk.Button(self, text="Back", command=self.go_back, style="TButton")
        self.back_button.pack()

    def go_back(self):
        self.students_view.set_students(get_students())
        self.master.switch_frame(view.StudentsView)
