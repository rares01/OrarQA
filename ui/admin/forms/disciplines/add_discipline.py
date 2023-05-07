import tkinter as tk
from tkinter import ttk
import ui.admin.views.disciplines_view as view
from repositories.discipline_repo import add_discipline


def handle(name_entry=None):
    name = name_entry.get()
    add_discipline(name=name)


class AddDisciplineForm(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.back_button = None
        self.display()

    def display(self):
        title_label = ttk.Label(self, text="Add Discipline Form", font=("Helvetica", 20))
        title_label.pack(pady=20)
        style = ttk.Style()
        style.configure('TLabel', font=('Helvetica', 14), padding=10)
        style.configure('TEntry', font=('Helvetica', 14), padding=10)
        style.configure('TCombobox', font=('Helvetica', 14), padding=10)
        style.configure('TButton', font=('Helvetica', 14), padding=10)
        name_label = ttk.Label(self, text="Name:")
        name_entry = ttk.Entry(self)

        name_label.pack()
        name_entry.pack()

        add_student_button = ttk.Button(self, text="Add", command=handle)
        add_student_button.pack()

        self.back_button = ttk.Button(self, text="Back", command=self.go_back, style="TButton")
        self.back_button.pack()

    def go_back(self):
        self.master.switch_frame(view.DisciplinesView)