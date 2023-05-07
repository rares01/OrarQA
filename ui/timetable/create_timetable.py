import tkinter as tk
from tkinter import ttk

import ui.timetable.timetable_page as timetable
from repositories.room_repo import get_room_values
from repositories.room_type_repo import get_room_type_values
from repositories.time_slot_repo import get_time_slot_values


class CreateTimetable(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.label_room = None
        self.label_professor = None
        self.label_type = None
        self.label_discipline = None
        self.type_options = None
        self.room_options = None
        self.teacher_options = None
        self.discipline_options = None
        self.time_options = None
        self.go_to_home = None
        self.button = None
        self.back_button = None
        self.label = None
        self.entry_labels = None
        self.label_timeslot = None
        self.frame = None
        self.master = master
        self.weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        self.entries = [[] for i in range(len(self.weekdays))]
        self.title_label = None
        self.style = None
        self.display()

    def display(self):
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("Helvetica", 14), padding=10)
        self.style.configure("TFrame", padding=10)
        self.style.configure("TButton", font=("Helvetica", 12), padding=10)

        # Create a frame for the weekdays
        self.frame = tk.Frame(self)
        self.frame.pack(side="left", fill="y", padx=10, pady=10)
        # Create labels and buttons for each weekday
        self.label_timeslot = tk.Label(self.frame, text="TimeSlot", font=("Arial", 14, "bold"))
        self.label_timeslot.grid(row=0, column=2, padx=10, pady=10, sticky="w", columnspan=4)

        self.label_discipline = tk.Label(self.frame, text="Discipline", font=("Arial", 14, "bold"))
        self.label_discipline.grid(row=0, column=6, padx=10, pady=10, sticky="w", columnspan=4)

        self.label_type = tk.Label(self.frame, text="Type", font=("Arial", 14, "bold"))
        self.label_type.grid(row=0, column=10, padx=10, pady=10, sticky="w", columnspan=4)

        self.label_professor = tk.Label(self.frame, text="Professor", font=("Arial", 14, "bold"))
        self.label_professor.grid(row=0, column=14, padx=10, pady=10, sticky="w", columnspan=4)

        self.label_room = tk.Label(self.frame, text="Room", font=("Arial", 14, "bold"))
        self.label_room.grid(row=0, column=18, padx=10, pady=10, sticky="w", columnspan=4)

        self.entry_labels = []
        for i, day in enumerate(self.weekdays):

            # Create a label for the weekday
            self.label = tk.Label(self.frame, text=day, font=("Arial", 14, "bold"))
            self.label.grid(row=i + 1, column=0, padx=10, pady=10, sticky="w")

            # Create a button to add entries for the weekday
            self.button = tk.Button(self.frame, text="Add Entry", command=lambda day=day: self.display_form(day))
            self.button.grid(row=i + 1, column=4, padx=10, pady=10, sticky="w")

            # Create a label for the entries for the weekday
            for j in range(5):
                entry_label = tk.Label(self.frame, text="", font=("Arial", 12))
                entry_label.grid(row=i + 1, column=j * 4 + 8, padx=10, pady=10, sticky="w", columnspan=4)
                self.entry_labels.append(entry_label)

        self.back_button = ttk.Button(self, text="Back", command=self.go_to_timetables, style="TButton")
        self.back_button.pack(side="bottom")

    def display_form(self, day):
        # Create a new window for the form
        window = tk.Toplevel()
        window.title("Add Entry for {day}")

        # Create a label for the form
        label1 = tk.Label(window, text="Time Slot:")
        label1.pack(pady=5, anchor="w")

        # Create a dropdown menu for time slot
        self.time_options = get_time_slot_values()
        time_var = tk.StringVar()
        time_var.set(self.time_options[0])
        time_dropdown = ttk.OptionMenu(window, time_var, *self.time_options)
        time_dropdown.pack(pady=5)

        # Create a label for the form
        label2 = tk.Label(window, text="Discipline:")
        label2.pack(pady=5, anchor="w")

        # Create a dropdown menu for discipline
        self.discipline_options = ["Math", "PE", "Sports", "Literature"]
        discipline_var = tk.StringVar()
        discipline_dropdown = ttk.OptionMenu(window, discipline_var, *self.discipline_options)
        discipline_dropdown.pack(pady=5)

        # Create a label for the form
        label3 = tk.Label(window, text="Type:")
        label3.pack(pady=5, anchor="w")

        # Create a dropdown menu for type
        self.type_options = get_room_type_values()
        type_var = tk.StringVar()
        type_var.set(self.type_options[0])
        type_dropdown = ttk.OptionMenu(window, type_var, *self.type_options)
        type_dropdown.pack(pady=5)

        label4 = tk.Label(window, text="Professor:")
        label4.pack(pady=5, anchor="w")

        # Create a dropdown menu for room
        self.teacher_options = ["Marcus", "Tiberius", "Augustus"]
        teacher_var = tk.StringVar()
        teacher_var.set(self.teacher_options[0])
        teacher_dropdown = ttk.OptionMenu(window, teacher_var, *self.teacher_options)
        teacher_dropdown.pack(pady=5)

        # Create a label for the form
        label5 = tk.Label(window, text="Room:")
        label5.pack(pady=5, anchor="w")

        # Create a dropdown menu for room
        self.room_options = get_room_values()
        room_var = tk.StringVar()
        room_var.set(self.room_options[0])
        room_dropdown = ttk.OptionMenu(window, room_var, *self.room_options)
        room_dropdown.pack(pady=5)

        # Create a function to handle form submission
        def submit_form():
            time_slot = time_var.get()
            discipline = discipline_var.get()
            form_type = type_var.get()
            room = room_var.get()
            teacher = teacher_var.get()
            add_entry(day, time_slot, discipline, teacher, form_type, room)
            window.destroy()

        # Create a button to submit the form
        self.button = tk.Button(window, text="Add Entry", command=submit_form)
        self.button.pack(pady=10)

        def add_entry(day, time_slot, discipline, teacher, form_type, room):
            # Find the index of the day in the weekdays list
            index = self.weekdays.index(day)

            # Add the entry to the list of entries for the day
            self.entries[index].append((time_slot, discipline, teacher, form_type, room))
            # Update the label for the day with the new entries
            update_label(day)

        # Create a function to update the label for a weekday
        def update_label(day):
            # Find the index of the day in the weekdays list
            index = self.weekdays.index(day)
            # Get the list of entries for the day
            day_entries = self.entries[index]
            final_time_slot = ""
            final_discipline = ""
            final_teacher = ""
            final_form_type = ""
            final_room = ""
            for entry in day_entries:
                time_slot, discipline, teacher, form_type, room = entry
                final_time_slot = final_time_slot + "\n" + time_slot
                final_discipline = final_discipline + "\n" + discipline
                final_teacher = final_teacher + "\n" + teacher
                final_form_type = final_form_type + "\n" + form_type
                final_room = final_room + "\n" + room

            self.entry_labels[index * 5].config(text=final_time_slot)
            self.entry_labels[index * 5 + 1].config(text=final_discipline)
            self.entry_labels[index * 5 + 2].config(text=final_teacher)
            self.entry_labels[index * 5 + 3].config(text=final_form_type)
            self.entry_labels[index * 5 + 4].config(text=final_room)

    def go_to_timetables(self):
        self.master.switch_frame(timetable.TimeTablePage)
