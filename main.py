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
from Login import Login
from SpeedTest import SpeedTest
from UserTests import UserTests
from TestsComparison import TestsComparison

LARGEFONT = ("Verdana", 35)

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.connection = None
        self.logged_in = tk.BooleanVar(value=False)
        self.username = tk.StringVar(value='')
        self.login_text = tk.StringVar(value='Prisijungti')

        self.title("OBD diagnostika")
        self.geometry("800x500")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Parameters, Tests, Profile, Settings, Gauge, Graph, Login, SpeedTest, UserTests, TestsComparison):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def connect(self):
        self.connection = obd.Async('/dev/ttys001')
        return self.connection.status() == OBDStatus.CAR_CONNECTED

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def show_parameter(self, cont, parameter):
        frame = self.frames[cont]
        frame.tkraise()
        frame.start(self.connection, parameter)

    def show_tests_comparison(self, cont, test1, test2):
        frame = self.frames[cont]
        frame.tkraise()
        frame.start(test1, test2)


    def show_login(self, cont):
        if self.is_logged_in():
            self.logout()
        else:
            frame = self.frames[cont]
            frame.tkraise()

    def login(self, username):
        self.logged_in.set(True)
        self.username.set(username)
        self.login_text.set('Atsijungti')

    def logout(self):
        self.logged_in.set(False)
        self.username.set('')
        self.login_text.set('Prisijungti')

    def is_logged_in(self):
        return self.logged_in.get()

if __name__ == "__main__":
    app = Application()
    app.mainloop()
