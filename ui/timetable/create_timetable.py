import random
import tkinter as tk
import webbrowser
from tkinter import ttk

import ui.timetable.timetable_page as timetable
from entities.scheduler_entry import SchedulerEntry
from repositories.room_repo import get_room_values
from repositories.room_type_repo import get_room_type_values
from repositories.scheduler_entry_repo import get_entries, get_entries_with_entity
from repositories.time_slot_repo import get_time_slot_values
from repositories.weekdays_repo import get_weekdays_values


class CreateTimetable(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.semi_year_options = None
        self.year_options = None
        self.teacher_options = None
        self.type_options = None
        self.time_options = None
        self.discipline_options = None
        self.group_options = None
        self.room_options = None
        self.back_button = None
        self.frame = None
        self.treeview = None
        self.master = master
        self.weekdays = get_weekdays_values()
        self.entries = [[] for i in range(len(self.weekdays))]
        self.title_label = None
        self.style = None
        self.scheduler = random.randint(0, 100)
        self.display()

    def display(self):
        self.style = ttk.Style()
        self.style.configure("Treeview", font=("Helvetica", 14), padding=10)
        self.style.configure("TFrame", padding=10)
        self.style.configure("TButton", font=("Helvetica", 12), padding=10)

        self.frame = ttk.Frame(self)
        self.frame.pack(side="left", fill="y", padx=10, pady=10)

        self.treeview = ttk.Treeview(self.frame, columns=("TimeSlot", "Discipline", "Type", "Professor", "Room"),
                                     show="headings")
        self.treeview.heading("TimeSlot", text="TimeSlot", anchor="center")
        self.treeview.heading("Discipline", text="Discipline", anchor="center")
        self.treeview.heading("Type", text="Type", anchor="center")
        self.treeview.heading("Professor", text="Professor", anchor="center")
        self.treeview.heading("Room", text="Room", anchor="center")

        for i, day in enumerate(self.weekdays):
            self.treeview.insert("", i, values=[day, "", "", "", ""])

        self.treeview.pack(side="left", fill="y")

        for i, day in enumerate(self.weekdays):
            button = ttk.Button(self.frame, text="Add Entry", command=lambda day=day: self.display_form(day), style="TButton")
            button.pack(side="top", pady=5)

        self.back_button = ttk.Button(self, text="Back", command=self.go_to_timetables, style="TButton")
        self.back_button.pack(side="bottom")


        self.back_button = ttk.Button(self, text="Generate HTML", command=self.go_to_html, style="TButton")
        self.back_button.pack(side="bottom", pady=8)



    def display_form(self, day):
        window = tk.Toplevel()
        window.title(f"Add Entry for {day}")

        label1 = tk.Label(window, text="Time Slot:")
        label1.pack(pady=5, anchor="w")

        self.time_options = get_time_slot_values()
        time_var = tk.StringVar()
        time_var.set(self.time_options[0])
        time_dropdown = ttk.OptionMenu(window, time_var, *self.time_options)
        time_dropdown.pack(pady=5)

        label2 = tk.Label(window, text="Discipline:")
        label2.pack(pady=5, anchor="w")

        self.discipline_options = ["Math", "PE", "Sports", "Literature"]
        discipline_var = tk.StringVar()
        discipline_dropdown = ttk.OptionMenu(window, discipline_var, *self.discipline_options)
        discipline_dropdown.pack(pady=5)

        label3 = tk.Label(window, text="Type:")
        label3.pack(pady=5, anchor="w")

        self.type_options = get_room_type_values()
        type_var = tk.StringVar()
        type_dropdown = ttk.OptionMenu(window, type_var, *self.type_options)
        type_dropdown.pack(pady=5)

        label4 = tk.Label(window, text="Professor:")
        label4.pack(pady=5, anchor="w")

        self.teacher_options = ["Marcus", "Tiberius", "Augustus"]
        teacher_var = tk.StringVar()
        teacher_dropdown = ttk.OptionMenu(window, teacher_var, *self.teacher_options)
        teacher_dropdown.pack(pady=5)

        label5 = tk.Label(window, text="Room:")
        label5.pack(pady=5, anchor="w")

        self.room_options = get_room_values()
        room_var = tk.StringVar()
        room_dropdown = ttk.OptionMenu(window, room_var, *self.room_options)
        room_dropdown.pack(pady=5)

        label6 = tk.Label(window, text="Year:")
        label6.pack(pady=5, anchor="w")

        self.year_options = ["Marcus", "Tiberius", "Augustus"]
        year_var = tk.StringVar()
        year_dropdown = ttk.OptionMenu(window, year_var, *self.year_options)
        year_dropdown.pack(pady=5)

        label7 = tk.Label(window, text="Semi Year:")
        label7.pack(pady=5, anchor="w")

        self.semi_year_options = ["Seria 1A", "Seria 1B", "Seria 1C"]
        semi_year_var = tk.StringVar()
        semi_year_var.set(self.semi_year_options[0])
        semi_year_dropdown = ttk.OptionMenu(window, semi_year_var, *self.semi_year_options)
        semi_year_dropdown.pack(pady=5)

        label7 = tk.Label(window, text="Group:")
        label7.pack(pady=5, anchor="w")

        self.group_options = ["None", "Grupa 1", "Grupa 2", "Grupa 3"]
        group_var = tk.StringVar()
        group_var.set(self.group_options[0])
        group_dropdown = ttk.OptionMenu(window, group_var, *self.group_options)
        group_dropdown.pack(pady=5)

        def submit_form():
            time_slot = time_var.get()
            discipline = discipline_var.get()
            form_type = type_var.get()
            teacher = teacher_var.get()
            room = room_var.get()
            add_entry(day, time_slot, discipline, teacher, form_type, room)
            window.destroy()

        button = tk.Button(window, text="Add Entry", command=submit_form)
        button.pack(pady=10)

        def add_entry(day, time_slot, discipline, teacher, form_type, room):
            self.treeview.insert("", "end", values=(time_slot, discipline, teacher, form_type, room))
            update_label(day)

        def update_label(day):
            index = self.weekdays.index(day)
            day_entries = self.entries[index]
            self.treeview.item(index, values=[day, "", "", "", ""])

            for i, entry in enumerate(day_entries):
                time_slot, discipline, teacher, form_type, room = entry
                self.treeview.item(index, values=[time_slot, discipline, teacher, form_type, room])

            self.treeview.config(font=("Helvetica", 12))

    def go_to_timetables(self):
        self.master.switch_frame(timetable.TimeTablePage)


    def go_to_html(self):

        # scheduler_entries = [
        #     SchedulerEntry(1, 'Monday', '09:00 - 11:00', 'John Doe', 'Mathematics', 2, 'Second', 1, 1),
        #     SchedulerEntry(2, 'Tuesday', '11:00 - 13:00', 'Jane Smith', 'English', 3, 'First', 2, 1),
        #     SchedulerEntry(3, 'Wednesday', '13:00 - 15:00', 'Bob Johnson', 'Physics', 2, 'Second', 1, 1),
        # ]

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

        # Open the HTML file in the default web browser
        webbrowser.open('my_html_file.html')


