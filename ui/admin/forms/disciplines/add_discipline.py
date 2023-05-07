import tkinter as tk
from tkinter import ttk

import ui.admin.views.disciplines_view as view
from repositories.discipline_repo import add_discipline
from repositories.study_year_repo import get_study_years_values
from repositories.teacher_repo import get_teacher_full_names


class AddDisciplineForm(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.back_button = None
        self.display()

    def handle(self, name_entry=None, year_entry=None, teacher_entry=None):
        name = name_entry.get()
        year = year_entry.get()
        teacher = teacher_entry.get()
        add_discipline(name=name, year=year, teacher=teacher)

    def display(self):
        title_label = ttk.Label(self, text="Add Discipline Form", font=("Helvetica", 20))
        title_label.pack(pady=20)
        style = ttk.Style()
        style.configure('TLabel', font=('Helvetica', 14), padding=10)
        style.configure('TEntry', font=('Helvetica', 14), padding=10)
        style.configure('TCombobox', font=('Helvetica', 14), padding=10)
        style.configure('TButton', font=('Helvetica', 14), padding=10)
        name_label = ttk.Label(self, text="Name:")
        study_year_label = ttk.Label(self, text="Year:")
        teacher_label = ttk.Label(self, text="Teacher:")
        name_entry = ttk.Entry(self)
        study_year_ids = get_study_years_values()
        study_year_var = tk.StringVar(self)
        study_year_var.set(study_year_ids[0])
        study_year_dropdown = ttk.Combobox(self, textvariable=study_year_var, values=study_year_ids, state='readonly')
        teacher_ids = get_teacher_full_names()
        teacher_var = tk.StringVar(self)
        teacher_var.set(study_year_ids[0])
        teacher_dropdown = ttk.Combobox(self, textvariable=teacher_var, values=teacher_ids, state='readonly')
        name_label.pack()
        name_entry.pack()
        study_year_label.pack()
        study_year_dropdown.pack()
        teacher_label.pack()
        teacher_dropdown.pack()

        add_discipline_button = ttk.Button(self, text="Add",
                                           command=lambda: self.handle(name_entry, study_year_dropdown,
                                                                       teacher_dropdown))
        add_discipline_button.pack()

        self.back_button = ttk.Button(self, text="Back", command=self.go_back, style="TButton")
        self.back_button.pack()

    def go_back(self):
        self.master.switch_frame(view.DisciplinesView)
