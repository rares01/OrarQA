import tkinter as tk
from tkinter import ttk

from repositories.student_repo import get_students
import ui.admin.admin_page as admin
from ui.admin.forms.students.add_students import AddStudentForm


class StudentsView(tk.Frame):
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
        students = get_students()

        title_label = ttk.Label(self, text="Students View", font=("Helvetica", 20))
        title_label.pack(pady=20)

        self.tree = ttk.Treeview(self, columns=("ID", "First Name", "Last Name", "Study Year", "Semi Year", "Student "
                                                                                                            "Group"),
                                 show="headings")
        self.tree.pack(padx=10, pady=10, fill="both", expand=True)

        for col in ("ID", "First Name", "Last Name", "Study Year", "Semi Year", "Student Group"):
            self.tree.heading(col, text=col, anchor="center")

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Helvetica", 16))
        style.configure("Treeview", font=("Helvetica", 12))

        for student in students:
            self.tree.insert("", "end", values=(student.id, student.first_name, student.last_name, student.study_year, student.semi_year, student.student_group))

        self.add_button = ttk.Button(self, text="Add", command=self.add_student, style="Custom.TButton")
        self.add_button.pack(side="top", pady=10)

        self.edit_button = ttk.Button(self, text="Edit", command=self.edit_student, state="disabled", style="Custom"
                                                                                                            ".TButton")
        self.edit_button.pack(side="left", padx=10, pady=10)

        self.delete_button = ttk.Button(self, text="Delete", command=self.delete_student, state="disabled", style="Custom.TButton")
        self.delete_button.pack(side="left", padx=10, pady=10)

        self.back_button = ttk.Button(self, text="Back", command=self.go_back, style="Custom.TButton")
        self.back_button.pack(side="right", padx=10, pady=10)

        self.tree.bind("<ButtonRelease-1>", self.on_tree_select)

        style.configure("Custom.TButton", font=("Helvetica", 12), background="#d8d8d8", foreground="#333", borderwidth=0, focuscolor="#d8d8d8", lightcolor="#d8d8d8", darkcolor="#d8d8d8")

    def on_tree_select(self, event):
        selection = self.tree.selection()
        if selection:
            self.edit_button.config(state="enabled")
            self.delete_button.config(state="enabled")
        else:
            self.edit_button.config(state="disabled")
            self.delete_button.config(state="disabled")

    def add_student(self):
        self.master.switch_frame(AddStudentForm)

    def go_back(self):
        self.master.switch_frame(admin.AdminPage)

    def edit_student(self):
        selection = self.tree.selection()
        if selection:
            values = self.tree.item(selection)["values"]
            print(f"Edit student {values[1]} {values[2]}")

    def delete_student(self):
        selection = self.tree.selection()
        if selection:
            values = self.tree.item(selection)["values"]
            print(f"Delete student {values[1]} {values[2]}")
