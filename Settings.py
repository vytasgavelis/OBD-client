import tkinter as tk
from tkinter import ttk
import StartPage
import requests
import json
from SettingModel import SettingModel

LARGEFONT = ("Verdana", 35)


class Settings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.settings = None

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

            can_compare_tests = tk.StringVar(value=r['settings']['can_compare_tests'])
            can_compare_tests_check = ttk.Checkbutton(self, text='Naudoti jusu testus palyginimui',
                                    variable=can_compare_tests,
                                    onvalue='1', offvalue='0').grid(row = 3, column=1)
