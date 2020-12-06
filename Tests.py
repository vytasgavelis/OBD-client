import tkinter as tk
from tkinter import ttk
import StartPage
import SpeedTest
import UserTests

LARGEFONT = ("Verdana", 35)

class Tests(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Testai", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        button2 = ttk.Button(self, text="Pradinis",
                             command=lambda: controller.show_frame(StartPage.StartPage))
        button2.grid(row=2, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Testas 0-60 km/h",
                             command=lambda: controller.show_parameter(SpeedTest.SpeedTest, 'SPEED'))
        button2.grid(row=3, column=1, padx=10, pady=10)

        self.user_tests_button = ttk.Button(self, text="Jusu testai",
                             command=lambda: controller.show_user_tests(UserTests.UserTests))
        self.user_tests_button['state'] = tk.DISABLED
        self.user_tests_button.grid(row=4, column=1, padx=10, pady=10)
