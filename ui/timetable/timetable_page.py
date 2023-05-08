import tkinter as tk

import ui.home.home_page as home_page
import ui.timetable.create_timetable as create_timetable
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
        self.title_label = tk.Label(self, text="Timetable Page")
        self.title_label.grid(row=0, column=0)

        self.create_timetable_button = tk.Button(self, text="CREATE TIMETABLE", command=self.go_to_create)
        self.create_timetable_button.grid(row=1, column=0)

        self.see_timetable_button = tk.Button(self, text="SEE TIMETABLE")
        self.see_timetable_button.grid(row=2, column=0)

        self.back_button = tk.Button(self, text="BACK", command=self.go_back)
        self.back_button.grid(row=3, column=0)

    def go_back(self):
        self.master.switch_frame(home_page.HomePage)

    def go_to_create(self):
        self.master.switch_frame(timetable_view.TimetableView)
