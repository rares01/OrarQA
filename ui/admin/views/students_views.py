# import tkinter as tk
#
# from entities.student import Student
#
# class StudentsView(tk.Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.create_widgets()
#
# def display():
#     students = [
#         Student(1, "John", "Doe", 2021, 1, "A"),
#         Student(2, "Jane", "Doe", 2021, 2, "B"),
#         Student(3, "Bob", "Smith", 2022, 1, "A"),
#         Student(4, "Alice", "Johnson", 2022, 2, "B")
#     ]
#     root = tk.Tk()
#     root.title("Student View")
#
#     def edit_student(stud):
#         print(f"Edit {stud.first_name} {stud.last_name}")
#
#     def delete_student(stud):
#         print(f"Delete {stud.first_name} {stud.last_name}")
#
#     def add_student():
#         print("Add new student")
#
#     frame = tk.Frame(root)
#     frame.pack(padx=10, pady=10)
#     add_button = tk.Button(frame, text="Add", command=add_student)
#     add_button.pack(side="top", pady=10)
#     scrollbar = tk.Scrollbar(frame)
#     scrollbar.pack(side="right", fill="y")
#     listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set)
#     for student in students:
#         listbox.insert("end", f"{student.first_name} {student.last_name}")
#     listbox.pack(side="left", fill="both", expand=True)
#     scrollbar.config(command=listbox.yview)
#     for i, student in enumerate(students):
#         row_frame = tk.Frame(listbox)
#         row_frame.pack(fill="x")
#
#         name_label = tk.Label(row_frame, text=f"{student.first_name} {student.last_name}")
#         name_label.pack(side="left", padx=10)
#
#         edit_button = tk.Button(row_frame, text="Edit", command=lambda stud=student: edit_student(stud))
#         edit_button.pack(side="left")
#
#         delete_button = tk.Button(row_frame, text="Delete", command=lambda stud=student: delete_student(stud))
#         delete_button.pack(side="left")
#
#
# display()
