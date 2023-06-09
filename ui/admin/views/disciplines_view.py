import tkinter as tk
from tkinter import ttk

import ui.admin.admin_page as admin
from repositories.discipline_repo import get_disciplines, delete_discipline
from repositories.study_year_repo import get_study_years_values
from repositories.teacher_repo import get_teacher_full_names
from ui.admin.forms.disciplines.add_discipline import AddDisciplineForm


class DisciplinesView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.disciplines = None
        self.teachers_filter = None
        self.study_year_filter = None
        self.back_button = None
        self.tree = None
        self.add_button = None
        self.delete_button = None
        self.master = master
        self.display()

    def display(self):
        assert callable(get_disciplines), "get_disciplines() function should be defined"
        assert callable(get_study_years_values), "get_study_years_values() function should be defined"
        assert callable(get_teacher_full_names), "get_teacher_full_names() function should be defined"
        self.disciplines = get_disciplines()

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

        for discipline in self.disciplines:
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

        year_filter_label = ttk.Label(self, text="Filter by Year:", font=("Helvetica", 14))
        year_filter_label.pack(side="left")
        study_year_ids = get_study_years_values()
        study_year_ids.insert(0, "All")
        self.study_year_filter = ttk.Combobox(self, values=study_year_ids, state="readonly")
        self.study_year_filter.bind("<<ComboboxSelected>>", lambda event: self.apply_filters())
        self.study_year_filter.current(0)
        self.study_year_filter.pack(side="left", padx=5)

        teachers_label = ttk.Label(self, text="Filter by Teacher:", font=("Helvetica", 14))
        teachers_label.pack(side="left")
        teachers_ids = get_teacher_full_names()
        teachers_ids.insert(0, "All")
        self.teachers_filter = ttk.Combobox(self, values=teachers_ids, state="readonly")
        self.teachers_filter.bind("<<ComboboxSelected>>", lambda event: self.apply_filters())
        self.teachers_filter.current(0)
        self.teachers_filter.pack(side="left", padx=5)

        assert self.disciplines is not None, "self.disciplines should not be None"
        assert isinstance(title_label, ttk.Label), "title_label should be an instance of ttk.Label"
        assert isinstance(self.tree, ttk.Treeview), "self.tree should be an instance of ttk.Treeview"
        assert isinstance(style, ttk.Style), "style should be an instance of ttk.Style"
        assert isinstance(self.add_button, ttk.Button), "self.add_button should be an instance of ttk.Button"
        assert isinstance(self.delete_button, ttk.Button), "self.delete_button should be an instance of ttk.Button"
        assert isinstance(self.back_button, ttk.Button), "self.back_button should be an instance of ttk.Button"
        assert isinstance(self.study_year_filter,
                          ttk.Combobox), "self.study_year_filter should be an instance of ttk.Combobox"
        assert isinstance(self.teachers_filter,
                          ttk.Combobox), "self.teachers_filter should be an instance of ttk.Combobox"

    def set_disciplines(self, current_disciplines):
        assert isinstance(current_disciplines, list), "current_disciplines should be a list"

        self.disciplines = current_disciplines

        assert self.disciplines == current_disciplines, "self.disciplines should be set to current_disciplines"

    def on_tree_select(self):
        assert isinstance(self.tree, ttk.Treeview), "self.tree must be a valid ttk.Treeview object."
        assert isinstance(self.delete_button, ttk.Button), "self.delete_button must be a valid ttk.Button object."

        selection = self.tree.selection()
        if selection:
            self.delete_button.config(state="enabled")
        else:
            self.delete_button.config(state="disabled")

        assert isinstance(self.delete_button, ttk.Button), "self.delete_button must be a valid ttk.Button object."

    def apply_filters(self):
        assert isinstance(self.study_year_filter,
                          ttk.Combobox), "self.study_year_filter should be an instance of ttk.Combobox"
        assert isinstance(self.teachers_filter,
                          ttk.Combobox), "self.teachers_filter should be an instance of ttk.Combobox"

        year = self.study_year_filter.get()
        teacher = self.teachers_filter.get()

        filtered_disciplined = []

        for discipline in self.disciplines:
            if year != "All" and discipline.study_year != int(year):
                continue
            if teacher != "All" and discipline.teacher_full_name != teacher:
                continue

            filtered_disciplined.append(discipline)

        self.update_treeview(filtered_disciplined)

        assert isinstance(year, str), "year should be a string"
        assert isinstance(teacher, str), "teacher should be a string"

    def update_treeview(self, filtered_disciplines):
        assert isinstance(filtered_disciplines, list), "filtered_disciplines should be a list"

        self.tree.delete(*self.tree.get_children())
        for discipline in filtered_disciplines:
            self.tree.insert("", "end", values=(
                discipline.id, discipline.name, discipline.study_year, discipline.teacher_full_name))

        children = self.tree.get_children()
        assert len(children) == len(
            filtered_disciplines), "Number of treeview items should match the number of filtered disciplines"

        for i, discipline in enumerate(filtered_disciplines):
            item_values = self.tree.item(children[i])["values"]
            assert item_values == [discipline.id, discipline.name, discipline.study_year,
                                   discipline.teacher_full_name], "Mismatch in treeview item values"

    def add_discipline(self):
        self.master.switch_frame(AddDisciplineForm)

    def go_back(self):
        self.master.switch_frame(admin.AdminPage)

    def delete_discipline(self):
        selection = self.tree.selection()
        if selection:
            values = self.tree.item(selection)["values"]
            delete_discipline(values[0])
            assert all(discipline.id is not values[0] for discipline in get_disciplines())
        self.update_treeview(get_disciplines())
