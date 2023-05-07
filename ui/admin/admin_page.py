import tkinter as tk
from tkinter import ttk


class AdminPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.title_label = None
        self.style = None
        self.master = master
        self.display()

    def display(self):
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Helvetica", 14), padding=10)
        self.style.configure("TFrame", padding=10)
        self.style.configure("TButton", font=("Helvetica", 12), padding=10)

        self.title_label = ttk.Label(self, text="Timetable Admin page", style="TLabel")
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

    def redirect_to_views(self, entity_name):
        print(entity_name)
