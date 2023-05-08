import tkinter as tk
import webbrowser
from tkinter import ttk

import ui.home.home_page as home
from repositories.discipline_repo import get_disciplines_value
from repositories.scheduler_entry_repo import get_entries, get_entries_with_entity
from repositories.semi_year_repo import get_semi_years_values
from repositories.student_group_repo import get_student_groups_values
from repositories.study_year_repo import get_study_years_values
from repositories.teacher_repo import get_teacher_full_names
from repositories.time_slot_repo import get_time_slot_values
from repositories.weekdays_repo import get_weekdays_values
from ui.admin.forms.timetable.add_timetable_entry import AddTimetableEntryForm


def go_to_html():
    scheduler_entries = get_entries_with_entity()
    html = '<!DOCTYPE html>'

    html += '<html>\n'
    html += '<body>\n'

    html += '<table>\n'
    html += '<tr><th>Weekday</th><th>Time Slot</th><th>Teacher</th><th>Discipline</th>'
    html += '<th>Study Year</th><th>Semi Year</th><th>Student Group</th><th>Scheduler ID</th></tr>\n'
    for entry in scheduler_entries:
        html += f'<tr><td>{entry.weekday}</td><td>{entry.time_slot}</td>'
        html += f'<td>{entry.teacher_id}</td><td>{entry.discipline}</td><td>{entry.study_year_id}</td>'
        html += f'<td>{entry.semi_year}</td><td>{entry.student_group}</td><td>{entry.scheduler_id}</td></tr>\n'
    html += '</table>'

    html += '</body>\n'
    html += '</html>\n'

    with open('my_html_file.html', 'w') as f:
        f.write(html)

    webbrowser.open('my_html_file.html')


class TimetableView(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.generate_html = None
        self.semi_year_filter = None
        self.group_filter = None
        self.weekday_filter = None
        self.time_slot_filter = None
        self.teacher_filter = None
        self.discipline_filter = None
        self.study_year_filter = None
        self.timetable_entries = None
        self.back_button = None
        self.tree = None
        self.add_button = None
        self.delete_button = None
        self.master = master
        self.display()

    def display(self):

        self.timetable_entries = get_entries()

        title_label = ttk.Label(self, text="Timetable View", font=("Helvetica", 12))
        title_label.pack(pady=6)

        self.tree = ttk.Treeview(self, columns=(
            "ID", "Weekday", "Time Slot", "Teacher", "Discipline", "Study Year", "Semi Year", "Student "
                                                                                              "Group"),
                                 show="headings")
        self.tree.column('ID', width=50)
        self.tree.column('Weekday', width=50)
        self.tree.column('Time Slot', width=50)
        self.tree.column('Teacher', width=50)
        self.tree.column('Discipline', width=50)
        self.tree.column('Study Year', width=50)
        self.tree.column('Semi Year', width=50)
        self.tree.column('Student Group', width=50)
        self.tree.pack(fill="both", expand=True)

        for col in (
                "ID", "Weekday", "Time Slot", "Teacher", "Discipline", "Study Year", "Semi Year", "Student "
                                                                                                  "Group"):
            self.tree.heading(col, text=col, anchor="center")

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Helvetica", 16))
        style.configure("Treeview", font=("Helvetica", 12))

        for entry in self.timetable_entries:
            self.tree.insert("", "end", values=(
                entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6], entry[7]))

        self.add_button = ttk.Button(self, text="Add", command=self.add_timetable_entry, style="Custom.TButton")
        self.add_button.pack(side="top", pady=10)

        self.back_button = ttk.Button(self, text="Back", command=self.go_back, style="Custom.TButton")
        self.back_button.pack(side="right", padx=10, pady=10)

        self.generate_html = ttk.Button(self, text="Generate HTML", command=go_to_html, style="TButton")
        self.generate_html.pack(side="left", pady=6)

        self.tree.bind("<ButtonRelease-1>", self.on_tree_select)

        style.configure("Custom.TButton", font=("Helvetica", 8), background="#d8d8d8", foreground="#333",
                        borderwidth=0, focuscolor="#d8d8d8", lightcolor="#d8d8d8", darkcolor="#d8d8d8")

        weekday_filter_label = ttk.Label(self, text="Filter by Weekday:", font=("Helvetica", 14))
        weekday_filter_label.pack(side="left")
        weekday_ids = get_weekdays_values()
        weekday_ids.insert(0, "All")
        self.weekday_filter = ttk.Combobox(self, values=weekday_ids, state="readonly")
        self.weekday_filter.bind("<<ComboboxSelected>>", lambda event: self.apply_filters())
        self.weekday_filter.current(0)
        self.weekday_filter.pack(side="left", padx=5)

        time_slot_filter_label = ttk.Label(self, text="Filter by Time Slot:", font=("Helvetica", 14))
        time_slot_filter_label.pack(side="left")
        time_slot_ids = get_time_slot_values()
        time_slot_ids.insert(0, "All")
        self.time_slot_filter = ttk.Combobox(self, values=time_slot_ids, state="readonly")
        self.time_slot_filter.bind("<<ComboboxSelected>>", lambda event: self.apply_filters())
        self.time_slot_filter.current(0)
        self.time_slot_filter.pack(side="left", padx=5)

        teacher_filter_label = ttk.Label(self, text="Filter by Teacher:", font=("Helvetica", 14))
        teacher_filter_label.pack(side="left")
        teacher_ids = get_teacher_full_names()
        teacher_ids.insert(0, "All")
        self.teacher_filter = ttk.Combobox(self, values=teacher_ids, state="readonly")
        self.teacher_filter.bind("<<ComboboxSelected>>", lambda event: self.apply_filters())
        self.teacher_filter.current(0)
        self.teacher_filter.pack(side="left", padx=5)

        discipline_filter_label = ttk.Label(self, text="Filter by Discipline:", font=("Helvetica", 14))
        discipline_filter_label.pack(side="top")
        discipline_ids = get_disciplines_value()
        discipline_ids.insert(0, "All")
        self.discipline_filter = ttk.Combobox(self, values=discipline_ids, state="readonly")
        self.discipline_filter.bind("<<ComboboxSelected>>", lambda event: self.apply_filters())
        self.discipline_filter.current(0)
        self.discipline_filter.pack(side="top", padx=5)

        year_filter_label = ttk.Label(self, text="Filter by Year:", font=("Helvetica", 14))
        year_filter_label.pack(side="top")
        study_year_ids = get_study_years_values()
        study_year_ids.insert(0, "All")
        self.study_year_filter = ttk.Combobox(self, values=study_year_ids, state="readonly")
        self.study_year_filter.bind("<<ComboboxSelected>>", lambda event: self.apply_filters())
        self.study_year_filter.current(0)
        self.study_year_filter.pack(side="top", padx=5)

        semi_year_filter_label = ttk.Label(self, text="Filter by Semi Year:", font=("Helvetica", 14))
        semi_year_filter_label.pack(side="top")
        semi_year_ids = get_semi_years_values()
        semi_year_ids.insert(0, "All")
        self.semi_year_filter = ttk.Combobox(self, values=semi_year_ids, state="readonly")
        self.semi_year_filter.bind("<<ComboboxSelected>>", lambda event: self.apply_filters())
        self.semi_year_filter.current(0)
        self.semi_year_filter.pack(side="top", padx=5)

        group_filter_label = ttk.Label(self, text="Filter by Group:", font=("Helvetica", 14))
        group_filter_label.pack(side="top")
        group_ids = get_student_groups_values()
        group_ids.insert(0, "All")
        self.group_filter = ttk.Combobox(self, values=group_ids, state="readonly")
        self.group_filter.bind("<<ComboboxSelected>>", lambda event: self.apply_filters())
        self.group_filter.current(0)
        self.group_filter.pack(side="top", padx=5)

    def set_timetable_entries(self, current_timetable_entries):
        self.timetable_entries = current_timetable_entries

    def on_tree_select(self, event):
        selection = self.tree.selection()
        if selection:
            self.delete_button.config(state="enabled")
        else:
            self.delete_button.config(state="disabled")

    def apply_filters(self):
        weekday = self.weekday_filter.get()
        time_slot = self.time_slot_filter.get()
        teacher = self.teacher_filter.get()
        discipline = self.discipline_filter.get()
        year = self.study_year_filter.get()
        semi_year = self.semi_year_filter.get()
        group = self.group_filter.get()

        filtered_entries = []

        for entry in self.timetable_entries:
            if weekday != "All" and entry[1] != weekday:
                continue
            if time_slot != "All" and entry[2] != time_slot:
                continue
            if teacher != "All" and entry[3] != teacher:
                continue
            if discipline != "All" and entry[4] != discipline:
                continue
            if year != "All" and entry[5] != int(year):
                continue
            if group != "All" and entry[7] != int(group):
                continue
            if semi_year != "All" and entry[6] != semi_year:
                continue

            filtered_entries.append(entry)

        self.update_treeview(filtered_entries)

    def update_treeview(self, filtered_entries):
        self.tree.delete(*self.tree.get_children())
        for entry in filtered_entries:
            self.tree.insert("", "end", values=(
                entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6], entry[7]))

    def add_timetable_entry(self):
        self.master.switch_frame(AddTimetableEntryForm)

    def go_back(self):
        self.master.switch_frame(home.HomePage)
