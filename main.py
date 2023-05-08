import tkinter as tk

from ui.admin.admin_page import AdminPage
from ui.admin.forms.students.add_students import AddStudentForm
from ui.admin.forms.disciplines.add_discipline import AddDisciplineForm
from ui.admin.forms.teachers.add_teacher_form import AddTeacherForm
from ui.admin.views.disciplines_view import DisciplinesView
from ui.admin.views.students_view import StudentsView
from ui.admin.views.teachers_view import TeachersView
from ui.home.home_page import HomePage
from ui.timetable.timetable_page import TimeTablePage
from ui.admin.views.timetable_view import TimetableView
from ui.admin.forms.timetable.add_timetable_entry import AddTimetableEntryForm


class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.frames = None
        self.title("Timetable Application")
        self.geometry("1920x1080")
        self.create_frames()

    def create_frames(self):
        self.frames = {}

        for F in (HomePage, TimeTablePage, AddTimetableEntryForm, AdminPage, StudentsView, AddStudentForm, DisciplinesView, TimetableView,
                  AddDisciplineForm, TeachersView, AddTeacherForm, ):
            frame = F(self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.switch_frame(HomePage)

    def switch_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()


app = MainApplication()
app.mainloop()
