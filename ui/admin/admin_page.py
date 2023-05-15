import tkinter as tk
from tkinter import ttk

import ui.admin.views.students_view as students_view
import ui.home.home_page as home
import ui.admin.views.disciplines_view as disciplines_view
import ui.admin.views.teachers_view as teachers_view


class AdminPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.back_button = None
        self.title_label = None
        self.style = None
        self.master = master
        self.display()

    def display(self):
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Helvetica", 14), padding=10)
        self.style.configure("TFrame", padding=10)
        self.style.configure("TButton", font=("Helvetica", 12), padding=10)

        self.title_label = ttk.Label(self, text="Admin Page", style="TLabel")
        self.title_label.pack()
        names = ["Students", "Teachers", "Disciplines"]
        for name in names:
            row_frame = ttk.Frame(self, style="TFrame")
            row_frame.pack(side="top", pady=10)

            name_label = ttk.Label(row_frame, text=name, style="TLabel")
            name_label.pack(side="left")

            view_button = ttk.Button(row_frame, text="View",
                                     command=lambda entity_name=name: self.redirect_to_views(entity_name),
                                     style="TButton")
            view_button.pack(side="left")
        self.back_button = ttk.Button(self, text="Back", command=self.go_to_home, style="TButton")
        self.back_button.pack(side="bottom")

    def redirect_to_views(self, entity_name):
        if entity_name == "Students":
            self.master.switch_frame(students_view.StudentsView)

        elif entity_name == "Disciplines":
            self.master.switch_frame(disciplines_view.DisciplinesView)

        elif entity_name == "Teachers":
            self.master.switch_frame(teachers_view.TeachersView)

    def go_to_home(self):
        self.master.switch_frame(home.HomePage)
