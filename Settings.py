import tkinter as tk
from tkinter import ttk
import StartPage
import requests
import json
from SettingModel import SettingModel
from tkinter import messagebox

LARGEFONT = ("Verdana", 35)


class Settings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.settings = None
        self.controller = controller

        label = ttk.Label(self, text="Nustatymai", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        button2 = ttk.Button(self, text="Pradinis",
                             command=lambda: controller.show_frame(StartPage.StartPage))
        button2.grid(row=2, column=1, padx=10, pady=10)

    def start(self, user_id):
        r = requests.get('http://localhost:8080/OBD-server/api.php?action=get_user_settings&user_id=' + user_id).json()

        if r['success']:
            # self.settings = SettingModel(
            #     setting_id = r['settings']['id'],
            #     user_id = r['settings']['user_id'],
            #     can_compare_tests = r['settings']['can_compare_tests']
            # )

            self.can_compare_tests = tk.BooleanVar(value=r['settings']['can_compare_tests'])
            can_compare_tests_check = ttk.Checkbutton(self, text='Naudoti jusu testus palyginimui',
                                    variable=self.can_compare_tests,
                                    onvalue=True, offvalue=False).grid(row = 3, column=1)

            ttk.Button(self, text="Issaugoti",
                       command=lambda: self.on_save_button_click()).grid(row=4, column=1)

    def on_save_button_click(self):
        can_compare_tests = 'false'
        if self.can_compare_tests.get():
            can_compare_tests = 'true'

        r = requests.post(
            'http://localhost:8080/OBD-server/api.php?action=update_user_settings',
            {
                'user_id': self.controller.user_id,
                'can_compare_tests': can_compare_tests
            }
        ).json()

        if not r['success']:
            messagebox.showerror('Klaida', 'Nepavyko issaugoti nustatymu.')

        self.controller.show_frame(StartPage.StartPage)
