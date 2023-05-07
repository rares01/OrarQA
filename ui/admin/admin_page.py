import tkinter as tk
from tkinter import ttk

from ui.admin.views.student_groups_view import StudentGroupsView
from ui.admin.views.students_views import StudentsView
import ui.home.home_page as home
from ui.admin.views.disciplines_view import DisciplinesView


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
        names = ["Students", "Groups", "Teachers", "Disciplines", "Rooms"]
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
            self.master.switch_frame(StudentsView)

        elif entity_name == "Disciplines":
            self.master.switch_frame(DisciplinesView)

        elif entity_name == "Groups":
            self.master.switch_frame(StudentGroupsView)


        
    def go_to_home(self):
        self.master.switch_frame(home.HomePage)
