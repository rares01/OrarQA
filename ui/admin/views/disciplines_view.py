import tkinter as tk
from tkinter import ttk

from repositories.discipline_repo import get_disciplines
import ui.admin.admin_page as admin
from ui.admin.forms.disciplines.add_discipline import AddDisciplineForm


class DisciplinesView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.back_button = None
        self.tree = None
        self.add_button = None
        self.delete_button = None
        self.master = master
        self.display()

    def display(self):
        disciplines = get_disciplines()

        title_label = ttk.Label(self, text="Disciplines View", font=("Helvetica", 20))
        title_label.pack(pady=20)

        self.tree = ttk.Treeview(self, columns=("ID", "Name", "Year", "Teacher"),
                                 show="headings")
        self.tree.pack(padx=10, pady=10, fill="both", expand=True)

        for col in ("ID", "Name", "Year", "Teacher"):
            self.tree.heading(col, text=col, anchor="center")

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Helvetica", 16))
        style.configure("Treeview", font=("Helvetica", 12))

        for discipline in disciplines:
            self.tree.insert("", "end", values=(
            discipline.id, discipline.name, discipline.study_year, discipline.teacher_full_name))

        self.add_button = ttk.Button(self, text="Add", command=self.add_discipline, style="Custom.TButton")
        self.add_button.pack(side="top", pady=10)

        self.delete_button = ttk.Button(self, text="Delete", command=self.delete_discipline, state="disabled",
                                        style="Custom.TButton")
        self.delete_button.pack(side="left", padx=10, pady=10)

        self.back_button = ttk.Button(self, text="Back", command=self.go_back, style="Custom.TButton")
        self.back_button.pack(side="right", padx=10, pady=10)

        self.tree.bind("<ButtonRelease-1>", self.on_tree_select)

        style.configure("Custom.TButton", font=("Helvetica", 12), background="#d8d8d8", foreground="#333",
                        borderwidth=0, focuscolor="#d8d8d8", lightcolor="#d8d8d8", darkcolor="#d8d8d8")

    def on_tree_select(self, event):
        selection = self.tree.selection()
        if selection:
            self.delete_button.config(state="enabled")
        else:
            self.delete_button.config(state="disabled")

    def add_discipline(self):
        self.master.switch_frame(AddDisciplineForm)

    def go_back(self):
        self.master.switch_frame(admin.AdminPage)


    def delete_discipline(self):
        selection = self.tree.selection()
        if selection:
            values = self.tree.item(selection)["values"]
            print(f"Delete discipline {values[0]} {values[1]}")
