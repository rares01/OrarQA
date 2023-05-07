import tkinter as tk

from ui.admin.admin_page import AdminPage
from ui.admin.forms.students.add_students import AddStudentForm
from ui.admin.forms.disciplines.add_discipline import AddDisciplineForm
from ui.admin.views.disciplines_view import DisciplinesView
from ui.admin.views.student_groups_view import StudentGroupsView
from ui.admin.views.students_views import StudentsView
from ui.home.home_page import HomePage
from ui.timetable.timetable_page import TimeTablePage
from ui.timetable.create_timetable import CreateTimetable


class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.frames = None
        self.title("Timetable Application")
        self.geometry("1280x900")
        self.create_frames()

    def create_frames(self):
        self.frames = {}

        for F in (HomePage, TimeTablePage, AdminPage, StudentsView, AddStudentForm, DisciplinesView, AddDisciplineForm,
                  StudentGroupsView, CreateTimetable):
            frame = F(self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.switch_frame(HomePage)

    def switch_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()


app = MainApplication()
app.mainloop()
