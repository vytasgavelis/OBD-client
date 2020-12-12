import tkinter as tk
from tkinter import ttk
from Parameters import Parameters
from Profile import Profile
from Settings import Settings
from Tests import Tests
from Login import Login
from Register import Register

LARGEFONT = ("Verdana", 35)

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.connected = tk.BooleanVar()
        self.connected.set(False)

        self.user_name = tk.StringVar()
        self.user_name.set('Anon')
        self.car_brand = 'Automobilis'

        self.build_layout(controller)

    def connect(self):
        self.connected.set(self.controller.connect())

    def build_layout(self, controller):
        label = ttk.Label(self, text="Startpage", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        self.parameters_button = ttk.Button(self, text="Parametrai",
                                       command=lambda: controller.show_frame(Parameters))
        self.parameters_button.grid(row=1, column=1, padx=10, pady=10)
        self.parameters_button['state'] = tk.DISABLED

        tests_button = ttk.Button(self, text="Testai",
                                  command=lambda: controller.show_frame(Tests))
        tests_button.grid(row=2, column=1, padx=10, pady=10)

        profile_button = ttk.Button(self, text="Profilis",
                                    command=lambda: controller.show_frame(Profile))
        profile_button.grid(row=3, column=1, padx=10, pady=10)

        self.settings_button = ttk.Button(self, text="Nustatymai",
                                     command=lambda: controller.show_settings(Settings))
        self.settings_button.grid(row=4, column=1, padx=10, pady=10)
        self.settings_button['state'] = tk.DISABLED

        ttk.Label(self, textvariable=controller.username).grid(row=5, column=1, sticky=("we"))
        ttk.Button(self, textvariable=controller.login_text, command=lambda: controller.show_login(Login)).grid(row=5, column=2, sticky="w")
        ttk.Label(self, textvariable=controller.logged_in).grid(row=5, column=3, sticky=("we"))

        ttk.Button(self, text='Registruotis', command=lambda: controller.show_frame(Register)).grid(row=6,column=3)

        ttk.Label(self, text=self.car_brand).grid(row=7, column=1, sticky=("we"))
        ttk.Button(self, text="Prisijungti", command=self.connect).grid(row=7, column=2, sticky="w")
        ttk.Label(self, textvariable=self.connected).grid(row=7, column=3, sticky=("we"))


