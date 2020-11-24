import tkinter as tk
from tkinter import ttk
from Parameters import Parameters
from Profile import Profile
from Settings import Settings
from Tests import Tests

LARGEFONT = ("Verdana", 35)

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.connected = tk.BooleanVar()
        self.connected.set(False)
        self.logged_in = tk.BooleanVar()
        self.logged_in.set(False)
        self.user_name = tk.StringVar()
        self.user_name.set('Anon')
        self.car_brand = 'BMW 323i'

        self.build_layout(controller)

    def connect(self):
        self.connected.set(self.controller.connect())

    def login(self):
        self.logged_in.set(False)

    def build_layout(self, controller):
        label = ttk.Label(self, text="Startpage", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        parameters_button = ttk.Button(self, text="Parametrai",
                                       command=lambda: controller.show_frame(Parameters))
        parameters_button.grid(row=1, column=1, padx=10, pady=10)

        tests_button = ttk.Button(self, text="Testai",
                                  command=lambda: controller.show_frame(Tests))
        tests_button.grid(row=2, column=1, padx=10, pady=10)

        profile_button = ttk.Button(self, text="Profilis",
                                    command=lambda: controller.show_frame(Profile))
        profile_button.grid(row=3, column=1, padx=10, pady=10)

        settings_button = ttk.Button(self, text="Nustatymai",
                                     command=lambda: controller.show_frame(Settings))
        settings_button.grid(row=4, column=1, padx=10, pady=10)

        ttk.Label(self, textvariable=self.user_name).grid(row=5, column=1, sticky=("we"))
        ttk.Button(self, text="Prisijungti", command=self.login).grid(row=5, column=2, sticky="w")
        ttk.Label(self, textvariable=self.logged_in).grid(row=5, column=3, sticky=("we"))

        ttk.Label(self, text=self.car_brand).grid(row=6, column=1, sticky=("we"))
        ttk.Button(self, text="Prisijungti", command=self.connect).grid(row=6, column=2, sticky="w")
        ttk.Label(self, textvariable=self.connected).grid(row=6, column=3, sticky=("we"))