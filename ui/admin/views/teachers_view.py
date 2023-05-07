import tkinter as tk
from tkinter import ttk

import ui.admin.admin_page as admin
from repositories.teacher_repo import get_full_teachers
from ui.admin.forms.teachers.add_teacher_form import AddTeacherForm


class TeachersView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.back_button = None
        self.tree = None
        self.add_button = None
        self.edit_button = None
        self.delete_button = None
        self.master = master
        self.display()

    def display(self):
        teachers = get_full_teachers()

        title_label = ttk.Label(self, text="Teachers View", font=("Helvetica", 20))
        title_label.pack(pady=20)

        self.tree = ttk.Treeview(self, columns=("ID", "First Name", "Last Name"),
                                 show="headings")
        self.tree.pack(padx=10, pady=10, fill="both", expand=True)

        for col in ("ID", "First Name", "Last Name"):
            self.tree.heading(col, text=col, anchor="center")

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Helvetica", 16))
        style.configure("Treeview", font=("Helvetica", 12))

        for teacher in teachers:
            self.tree.insert("", "end", values=(
            teacher.id, teacher.first_name, teacher.last_name))

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
            self.edit_button.config(state="enabled")
            self.delete_button.config(state="enabled")
        else:
            self.edit_button.config(state="disabled")
            self.delete_button.config(state="disabled")

    def add_discipline(self):
        self.master.switch_frame(AddTeacherForm)

    def go_back(self):
        self.master.switch_frame(admin.AdminPage)


    def delete_discipline(self):
        selection = self.tree.selection()
        if selection:
            values = self.tree.item(selection)["values"]
            print(f"Delete discipline {values[0]} {values[1]}")
