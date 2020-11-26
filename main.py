import obd
from obd import OBDStatus
import tkinter as tk
from StartPage import StartPage
from Parameters import Parameters
from Profile import Profile
from Settings import Settings
from Tests import Tests
from Gauge import Gauge
from Graph import Graph

LARGEFONT = ("Verdana", 35)

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.connection = None

        self.title("OBD diagnostika")
        self.geometry("800x500")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Parameters, Tests, Profile, Settings, Gauge, Graph):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def connect(self):
        self.connection = obd.Async('/dev/ttys002')
        return self.connection.status() == OBDStatus.CAR_CONNECTED

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def show_parameter(self, cont, parameter):
        frame = self.frames[cont]
        frame.tkraise()
        frame.start(self.connection, parameter)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
