import tkinter as tk
from tkinter import ttk

import ui.home.home_page as home_page
import ui.timetable.timetable_page as timetable


class SelectYear(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.groups = ["Grupa 1", "Grupa 2", "Grupa 3"]
        self.style = None
        self.back_button = None
        self.years = ["Anul 1", "Anul 2", "Anul 3"]
        self.series = ["Seria 1A", "Seria 2A", "Seria 3A"]
        self.display()

    def display(self):
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Helvetica", 14), padding=10)
        self.style.configure("TFrame", padding=10)
        self.style.configure("TButton", font=("Helvetica", 12), padding=10)
        # Create the labels
        for i, year in enumerate(self.years):
            label = ttk.Button(self, text=year, command=self.go_to_timetable, style="TLabel")
            label.pack(side="top", fill="x", padx=10, pady=10)

            for j, series in enumerate(self.series):
                series_label = ttk.Button(self, text=series, command=self.go_to_timetable, style="TLabel")
                series_label .pack(side="top", padx=30)

                for k, group in enumerate(self.groups):
                    groups_label = ttk.Button(self, text=group, command=self.go_to_timetable, style="TLabel")
                    groups_label.pack(side="top", padx=30)

            # Add a separator between each year
            if i != len(self.years) - 1:
                separator = ttk.Separator(self, orient="horizontal")
                separator.pack(fill="x", pady=10)

        self.back_button = ttk.Button(self, text="Back", command=self.go_to_home, style="TButton")
        self.back_button.pack(side="bottom")

    def go_to_timetable(self):
        self.master.switch_frame(timetable.TimeTablePage)

    def go_to_home(self):
        self.master.switch_frame(home_page.HomePage)
