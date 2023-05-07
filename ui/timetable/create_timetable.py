import tkinter as tk
from tkinter import ttk

# Create a list of weekdays
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]


# Create a function to display the form
def display_form(day):
    # Create a new window for the form
    window = tk.Toplevel()
    window.title(f"Add Entry for {day}")

    # Create a label for the form
    label1 = tk.Label(window, text="Time Slot:")
    label1.pack(pady=5, anchor="w")

    # Create a dropdown menu for time slot
    time_options = ["8:00-10:00", "10:00-12:00", "12:00-14:00", "14:00-16:00", "16:00-18:00", "18:00-20:00"]
    time_var = tk.StringVar()
    time_var.set(time_options[0])
    print(time_options)
    time_dropdown = ttk.OptionMenu(window, time_var, *time_options)
    time_dropdown.pack(pady=5)

    # Create a label for the form
    label2 = tk.Label(window, text="Discipline:")
    label2.pack(pady=5, anchor="w")

    # Create a dropdown menu for discipline
    discipline_options = ["Math", "PE", "Sports", "Literature"]
    discipline_var = tk.StringVar()
    discipline_dropdown = ttk.OptionMenu(window, discipline_var, *discipline_options)
    discipline_dropdown.pack(pady=5)

    # Create a label for the form
    label3 = tk.Label(window, text="Type:")
    label3.pack(pady=5, anchor="w")

    # Create a dropdown menu for type
    type_options = ["course", "laboratory", "seminary"]
    type_var = tk.StringVar()
    type_var.set(type_options[0])
    type_dropdown = ttk.OptionMenu(window, type_var, *type_options)
    type_dropdown.pack(pady=5)

    label4 = tk.Label(window, text="Professor:")
    label4.pack(pady=5, anchor="w")

    # Create a dropdown menu for room
    teacher_options = ["Marcus", "Tiberius", "Augustus"]
    teacher_var = tk.StringVar()
    teacher_var.set(teacher_options[0])
    teacher_dropdown = ttk.OptionMenu(window, teacher_var, *teacher_options)
    teacher_dropdown.pack(pady=5)

    # Create a label for the form
    label5 = tk.Label(window, text="Room:")
    label5.pack(pady=5, anchor="w")

    # Create a dropdown menu for room
    room_options = ["C11", "S11", "C3"]
    room_var = tk.StringVar()
    room_var.set(room_options[0])
    room_dropdown = ttk.OptionMenu(window, room_var, *room_options)
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
    button = tk.Button(window, text="Add Entry", command=submit_form)
    button.pack(pady=10)


# Create a function to add an entry to a weekday
def add_entry(day, time_slot, discipline, teacher, form_type, room):
    # Find the index of the day in the weekdays list
    index = weekdays.index(day)

    # Add the entry to the list of entries for the day
    entries[index].append((time_slot, discipline, teacher, form_type, room))
    # Update the label for the day with the new entries
    update_label(day)


# Create a function to update the label for a weekday
def update_label(day):
    # Find the index of the day in the weekdays list
    index = weekdays.index(day)
    # Get the list of entries for the day
    day_entries = entries[index]
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

    entry_labels[index * 5].config(text=final_time_slot)
    entry_labels[index * 5 + 1].config(text=final_discipline)
    entry_labels[index * 5 + 2].config(text=final_teacher)
    entry_labels[index * 5 + 3].config(text=final_form_type)
    entry_labels[index * 5 + 4].config(text=final_room)


# Create a list to hold the entries for each day
entries = [[] for _ in range(len(weekdays))]

# Create the main window
root = tk.Tk()
root.title("Frame")
root.geometry("700x400")

# Create a frame for the weekdays
frame = tk.Frame(root)
frame.pack(side="left", fill="y", padx=10, pady=10)
# Create labels and buttons for each weekday
label_timeslot = tk.Label(frame, text="TimeSlot", font=("Arial", 14, "bold"))
label_timeslot.grid(row=0, column=2, padx=10, pady=10, sticky="w")

label_timeslot = tk.Label(frame, text="Discipline", font=("Arial", 14, "bold"))
label_timeslot.grid(row=0, column=3, padx=10, pady=10, sticky="w")

label_timeslot = tk.Label(frame, text="Type", font=("Arial", 14, "bold"))
label_timeslot.grid(row=0, column=4, padx=10, pady=10, sticky="w")

label_timeslot = tk.Label(frame, text="Professor", font=("Arial", 14, "bold"))
label_timeslot.grid(row=0, column=5, padx=10, pady=10, sticky="w")

label_timeslot = tk.Label(frame, text="Room", font=("Arial", 14, "bold"))
label_timeslot.grid(row=0, column=6, padx=10, pady=10, sticky="w")

entry_labels = []
for i, day in enumerate(weekdays):

    # Create a label for the weekday
    label = tk.Label(frame, text=day, font=("Arial", 14, "bold"))
    label.grid(row=i + 1, column=0, padx=10, pady=10, sticky="w")

    # Create a button to add entries for the weekday
    button = tk.Button(frame, text="Add Entry", command=lambda day=day: display_form(day))
    button.grid(row=i + 1, column=1, padx=10, pady=10, sticky="w")

    # Create a label for the entries for the weekday
    for j in range(5):
        entry_label = tk.Label(frame, text="", font=("Arial", 12))
        entry_label.grid(row=i + 1, column=j + 2, padx=10, pady=10, sticky="w")
        entry_labels.append(entry_label)

# Run the main loop
root.mainloop()
