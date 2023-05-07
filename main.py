import tkinter as tk
from ui.home.home_page import HomePage
from ui.timetable.timetable_page import TimeTablePage


class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Timetable Application")
        self.geometry("400x300")
        self.create_frames()

    def create_frames(self):
        self.frames = {}
        for F in (HomePage, TimeTablePage):
            frame = F(self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.switch_frame(HomePage)

    def switch_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()


app = MainApplication()
app.mainloop()
