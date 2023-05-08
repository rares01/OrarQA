import tkinter as tk
from tkinter import ttk

import ui.admin.views.timetable_view as view
from repositories.discipline_repo import get_disciplines, get_disciplines_value
from repositories.scheduler_entry_repo import add_entry, get_entries
from repositories.semi_year_repo import get_semi_years_values
from repositories.student_group_repo import get_student_groups_values
from repositories.student_repo import add_student, get_students
from repositories.study_year_repo import get_study_years_values
from repositories.teacher_repo import get_teacher_full_names
from repositories.time_slot_repo import get_time_slot_values
from repositories.weekdays_repo import get_weekdays_values


def handle(weekday_entry=None, time_slot_entry=None, teacher_entry=None, discipline_entry=None,
           study_year_entry=None, semi_year_entry=None, student_group_entry=None):
    weekday = weekday_entry.get()
    time_slot = time_slot_entry.get()
    start_hour, end_hour = time_slot.split('-')
    start_hour = start_hour.split(':')[0]
    end_hour = end_hour.split(':')[0]
    teacher = teacher_entry.get()
    discipline = discipline_entry.get()
    study_year = study_year_entry.get()
    semi_year = semi_year_entry.get()
    student_group = student_group_entry.get()
    add_entry(weekday=weekday, start_hour=start_hour, end_hour=end_hour, teacher=teacher, discipline=discipline,
              study_year=study_year, semi_year=semi_year, student_group=student_group, scheduler_id=1)


class AddTimetableEntryForm(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.back_button = None
        self.timetable_view = None
        for child in master.winfo_children():
            if isinstance(child, view.TimetableView):
                self.timetable_view = child
                break
        self.display()

    def display(self):
        title_label = ttk.Label(self, text="Add Timetable Entry Form", font=("Helvetica", 20))
        title_label.pack(pady=20)
        style = ttk.Style()
        style.configure('TLabel', font=('Helvetica', 14), padding=10)
        style.configure('TEntry', font=('Helvetica', 14), padding=10)
        style.configure('TCombobox', font=('Helvetica', 14), padding=10)
        style.configure('TButton', font=('Helvetica', 14), padding=10)
        weekday_label = ttk.Label(self, text="Weekday:")
        time_slot_label = ttk.Label(self, text="Time Slot:")
        teacher_label = ttk.Label(self, text="Professor:")
        discipline_label = ttk.Label(self, text="Discipline:")
        study_year_label = ttk.Label(self, text="Study Year:")
        semi_year_label = ttk.Label(self, text="Semi Year:")
        student_group_label = ttk.Label(self, text="Student Group:")
        weekday_ids = get_weekdays_values()
        weekday_var = tk.StringVar(self)
        weekday_var.set(weekday_ids[0])
        weekday_dropdown = ttk.Combobox(self, textvariable=weekday_var, values=weekday_ids, state='readonly')
        time_slot_ids = get_time_slot_values()
        time_slot_var = tk.StringVar(self)
        time_slot_var.set(time_slot_ids[0])
        time_slot_dropdown = ttk.Combobox(self, textvariable=time_slot_var, values=time_slot_ids, state='readonly')
        teacher_ids = get_teacher_full_names()
        teacher_var = tk.StringVar(self)
        teacher_var.set(teacher_ids[0])
        teacher_dropdown = ttk.Combobox(self, textvariable=teacher_var, values=teacher_ids, state='readonly')
        discipline_ids = get_disciplines_value()
        discipline_var = tk.StringVar(self)
        discipline_var.set(discipline_ids[0])
        discipline_dropdown = ttk.Combobox(self, textvariable=discipline_var, values=discipline_ids, state='readonly')
        study_year_ids = get_study_years_values()
        study_year_var = tk.StringVar(self)
        study_year_var.set(study_year_ids[0])
        study_year_dropdown = ttk.Combobox(self, textvariable=study_year_var, values=study_year_ids, state='readonly')
        semi_year_ids = get_semi_years_values()
        semi_year_var = tk.StringVar(self)
        semi_year_var.set(semi_year_ids[0])
        semi_year_dropdown = ttk.Combobox(self, textvariable=semi_year_var, values=semi_year_ids, state='readonly')
        student_group_ids = get_student_groups_values()
        student_group_var = tk.StringVar(self)
        student_group_var.set(student_group_ids[0])
        student_group_dropdown = ttk.Combobox(self, textvariable=student_group_var, values=student_group_ids,
                                              state='readonly')
        weekday_label.pack()
        weekday_dropdown.pack()
        time_slot_label.pack()
        time_slot_dropdown.pack()
        teacher_label.pack()
        teacher_dropdown.pack()
        discipline_label.pack()
        discipline_dropdown.pack()
        study_year_label.pack()
        study_year_dropdown.pack()
        semi_year_label.pack()
        semi_year_dropdown.pack()
        student_group_label.pack()
        student_group_dropdown.pack()
        add_timetable_entry_button = ttk.Button(self, text="Add Entry",
                                        command=lambda: handle(weekday_var, time_slot_var, teacher_var,
                                                               discipline_var, study_year_var, semi_year_var,
                                                               student_group_var))
        add_timetable_entry_button.pack()

        self.back_button = ttk.Button(self, text="Back", command=self.go_back, style="TButton")
        self.back_button.pack()

    def go_back(self):
        for child in self.master.winfo_children():
            if isinstance(child, view.TimetableView):
                self.timetable_view = child
                break
        self.timetable_view.set_timetable_entries(get_entries())
        self.master.switch_frame(view.TimetableView)
