import tkinter as tk
from tkinter import ttk
import StartPage
from tkinter import messagebox
import requests
import json

LARGEFONT = ("Verdana", 35)

class Profile(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg="#ECECEC")
        self.header_image = tk.PhotoImage(file='assets/profile.png')
        label = ttk.Label(self, image=self.header_image).grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Atgal",
                             command=lambda: controller.show_frame(StartPage.StartPage))
        button2.grid(row=2, column=1, padx=10, pady=10)

        self.test_count = tk.StringVar(value="Atlikta testų: 0")
        ttk.Label(self, textvariable=self.test_count).grid(row=3, column=1)

    def start(self, user_id):
        try:
            r = requests.get(
                'http://localhost:8080/OBD-server/api.php?action=get_tests&user_id=' + str(user_id),
                timeout=3
            ).json()

            if r['success']:
                self.test_count.set('Atlikta testų: ' + str(len(r['speed_tests'])))

        except requests.exceptions.RequestException:
            messagebox.showerror('Klaida', 'Tinklo klaida')
