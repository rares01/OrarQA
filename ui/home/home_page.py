import tkinter as tk
from tkinter import ttk

import ui.admin.admin_page as admin
import ui.timetable.select_year as select_year
import ui.timetable.timetable_page as timetable_page


class HomePage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.timetable_button = None
        self.admin_button = None
        self.title_label = None
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.title_label = ttk.Label(self, text="Home Page", font=("Helvetica", 20))
        self.title_label.pack(side="top", pady=10)

        self.admin_button = ttk.Button(self, text="Admin", command=self.go_to_admin_page, style="Custom.TButton")
        self.admin_button.pack(side="top", pady=10)

        self.timetable_button = ttk.Button(self, text="Timetable" , command=self.go_to_timetable, style="Custom.TButton")
        self.timetable_button.pack(side="top", pady=10)


    def go_to_admin_page(self):
        self.master.switch_frame(admin.AdminPage)

    def go_to_timetable(self):
        self.master.switch_frame(timetable_page.TimeTablePage)
