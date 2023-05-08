import tkinter as tk
from tkinter import ttk

import ui.admin.views.teachers_view as view
from repositories.teacher_repo import add_teacher


class AddTeacherForm(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.back_button = None
        self.display()

    def handle(self, first_name_entry=None, last_name_entry=None):
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        add_teacher(first_name=first_name, last_name=last_name)

    def display(self):
        title_label = ttk.Label(self, text="Add Discipline Form", font=("Helvetica", 20))
        title_label.pack(pady=20)
        style = ttk.Style()
        style.configure('TLabel', font=('Helvetica', 14), padding=10)
        style.configure('TEntry', font=('Helvetica', 14), padding=10)
        style.configure('TCombobox', font=('Helvetica', 14), padding=10)
        style.configure('TButton', font=('Helvetica', 14), padding=10)
        first_name_label = ttk.Label(self, text="First Name:")
        last_name_label = ttk.Label(self, text="Last Name:")
        first_name_entry = ttk.Entry(self)
        last_name_entry = ttk.Entry(self)

        first_name_label.pack()
        first_name_entry.pack()
        last_name_label.pack()
        last_name_entry.pack()

        add_teacher_button = ttk.Button(self, text="Add",
                                        command=lambda: self.handle(first_name_entry, last_name_entry))
        add_teacher_button.pack()

        self.back_button = ttk.Button(self, text="Back", command=self.go_back, style="TButton")
        self.back_button.pack()

    def go_back(self):
        self.master.switch_frame(view.TeachersView)
