import tkinter as tk
from tkinter import ttk
from Parameters import Parameters
from Profile import Profile
from Settings import Settings
from Tests import Tests
from Login import Login
from Register import Register
from PIL import Image
from PIL import ImageTk

LARGEFONT = ("Verdana", 35)
MEDIUMFONT = ("Verdana", 25)

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.configure(bg="#ECECEC")
        self.connected = tk.BooleanVar()
        self.connected.set(False)

        self.user_name = tk.StringVar()
        self.user_name.set('Anon')
        self.car_brand = tk.StringVar(value='Automobilis (neprisijungta)')

        self.build_layout(controller)

    def connect(self):
        self.connected.set(self.controller.connect())

    def build_layout(self, controller):
        self.logo_image = tk.PhotoImage(file='assets/header.png')
        ttk.Label(self, image=self.logo_image).grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        self.parameters_image = tk.PhotoImage(file='assets/parameters.png')
        self.tests_image = tk.PhotoImage(file='assets/tests.png')
        self.profile_image = tk.PhotoImage(file='assets/profile.png')
        self.settings_image = tk.PhotoImage(file='assets/settings.png')

        self.parameters_button = tk.Button(self, image=self.parameters_image,
                                       command=lambda: controller.show_frame(Parameters))
        self.parameters_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.parameters_button['state'] = tk.DISABLED

        tests_button = tk.Button(self, image=self.tests_image,
                                  command=lambda: controller.show_frame(Tests))
        tests_button.grid(row=1, column=3, columnspan=2, padx=10, pady=10)

        self.profile_button = tk.Button(self, image=self.profile_image,
                                    command=lambda: controller.show_profile(Profile))
        self.profile_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        self.profile_button['state'] = tk.DISABLED

        self.settings_button = tk.Button(self, image=self.settings_image,
                                     command=lambda: controller.show_settings(Settings))
        self.settings_button.grid(row=2, column=3, columnspan=2, padx=10, pady=10)
        self.settings_button['state'] = tk.DISABLED

        ttk.Label(self, textvariable=controller.username, width=18, borderwidth=2, relief="solid").grid(row=3, column=0)
        ttk.Button(self, textvariable=controller.login_text, width=17, command=lambda: controller.show_login(Login)).grid(row=3, column=1)

        ttk.Button(self, text='Registruotis', width=17, command=lambda: controller.show_frame(Register)).grid(row=4,column=1)

        ttk.Label(self, textvariable=self.car_brand, width=18, borderwidth=2, relief="solid").grid(row=3, column=3)
        ttk.Button(self, text="Prisijungti", width=17, command=self.connect).grid(row=3, column=4)
