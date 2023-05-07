import tkinter as tk
from ui.timetable.timetable_page import TimeTablePage

class HomePage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self, text="Home Page")
        self.title_label.grid(row=0, column=0)

        self.admin_button = tk.Button(self, text="ADMIN")
        self.admin_button.grid(row=1, column=0)

        self.timetable_button = tk.Button(self, text="TIMETABLE", command=self.go_to_timetable)
        self.timetable_button.grid(row=2, column=0)

    def go_to_timetable(self):
        self.master.switch_frame(TimeTablePage)
