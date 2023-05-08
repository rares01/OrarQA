import tkinter as tk
from tkinter import ttk

import ui.home.home_page as home_page
import ui.admin.views.timetable_view as timetable_view


class TimeTablePage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.back_button = None
        self.see_timetable_button = None
        self.create_timetable_button = None
        self.title_label = None
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.title_label = ttk.Label(self, text="Timetable Page", font=("Helvetica", 20))
        self.title_label.pack(side="top", pady=10)

        self.create_timetable_button = ttk.Button(self, text="Create Timetable", command=self.go_to_create, style="Custom.TButton")
        self.create_timetable_button.pack(side="top", pady=10)

        self.back_button = ttk.Button(self, text="Back", command=self.go_back, style="Custom.TButton")
        self.back_button.pack(side="bottom", pady=10)

    def go_back(self):
        self.master.switch_frame(home_page.HomePage)

    def go_to_create(self):
        self.master.switch_frame(timetable_view.TimetableView)
