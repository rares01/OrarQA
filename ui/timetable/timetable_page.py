import tkinter as tk
from ui.home.home_page import HomePage

class TimeTablePage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self, text="Timetable Page")
        self.title_label.grid(row=0, column=0)

        self.create_timetable_button = tk.Button(self, text="CREATE TIMETABLE")
        self.create_timetable_button.grid(row=1, column=0)

        self.see_timetable_button = tk.Button(self, text="SEE TIMETABLE")
        self.see_timetable_button.grid(row=2, column=0)

        self.back_button = tk.Button(self, text="BACK", command=self.go_to_home)
        self.back_button.grid(row=3, column=0)

    def go_to_home(self):
        self.master.switch_frame(HomePage)
