import tkinter as tk
from tkinter import ttk

from repositories.semi_year_repo import get_semi_years_values
from repositories.student_group_repo import get_student_groups_values
from repositories.student_repo import add_student
from repositories.study_year_repo import get_study_years_values


def handle():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    study_year = study_year_var.get()
    semi_year = semi_year_var.get()
    student_group = student_group_var.get()
    add_student(first_name=first_name, last_name=last_name, study_year=study_year, semi_year=semi_year,
                student_group=student_group)


root = tk.Tk()
root.title("Admin Page - Students Management Operations")

style = ttk.Style()
style.configure('TLabel', font=('Arial', 14), padding=10)
style.configure('TEntry', font=('Arial', 14), padding=10)
style.configure('TCombobox', font=('Arial', 14), padding=10)
style.configure('TButton', font=('Arial', 14), padding=10)

first_name_label = ttk.Label(root, text="First Name:")
last_name_label = ttk.Label(root, text="Last Name:")
study_year_label = ttk.Label(root, text="Study Year:")
semi_year_label = ttk.Label(root, text="Semi Year:")
student_group_label = ttk.Label(root, text="Student Group:")

first_name_entry = ttk.Entry(root)
last_name_entry = ttk.Entry(root)

study_year_ids = get_study_years_values()
study_year_var = tk.StringVar(root)
study_year_var.set(study_year_ids[0])
study_year_dropdown = ttk.Combobox(root, textvariable=study_year_var, values=study_year_ids, state='readonly')

semi_year_ids = get_semi_years_values()
semi_year_var = tk.StringVar(root)
semi_year_var.set(semi_year_ids[0])
semi_year_dropdown = ttk.Combobox(root, textvariable=semi_year_var, values=semi_year_ids, state='readonly')

student_group_ids = get_student_groups_values()
student_group_var = tk.StringVar(root)
student_group_var.set(student_group_ids[0])
student_group_dropdown = ttk.Combobox(root, textvariable=student_group_var, values=student_group_ids, state='readonly')

first_name_label.grid(row=0, column=0)
first_name_entry.grid(row=0, column=1)
last_name_label.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)
study_year_label.grid(row=2, column=0)
study_year_dropdown.grid(row=2, column=1)
semi_year_label.grid(row=3, column=0)
semi_year_dropdown.grid(row=3, column=1)
student_group_label.grid(row=4, column=0)
student_group_dropdown.grid(row=4, column=1)

add_student_button = ttk.Button(root, text="Add Student", command=handle)

add_student_button.grid(row=5, column=1)

root.mainloop()
