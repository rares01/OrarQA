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

        assert isinstance(self.title_label, ttk.Label), "title_label should be an instance of ttk.Label"
        assert isinstance(self.admin_button, ttk.Button), "self.admin_button should be an instance of ttk.Button"
        assert isinstance(self.timetable_button, ttk.Button), "self.timetable_button should be an instance of " \
                                                              "ttk.Button"




    def go_to_admin_page(self):
        assert hasattr(self.master, "switch_frame"), "self.master should have the 'switch_frame' method"

        self.master.switch_frame(admin.AdminPage)
        assert self.master.current_frame == admin.AdminPage, "Expected current_frame to be set to AdminPage"


    def go_to_timetable(self):
        assert hasattr(self.master, "switch_frame"), "self.master should have the 'switch_frame' method"

        self.master.switch_frame(timetable_page.TimeTablePage)
        assert self.master.current_frame == timetable_page.TimeTablePage, "Expected current_frame to be set to TimeTablePage"
