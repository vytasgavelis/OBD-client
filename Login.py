import tkinter as tk
from tkinter import ttk
import StartPage
import requests

LARGEFONT = ("Verdana", 35)

class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.email = tk.StringVar()
        self.password = tk.StringVar()
        self.errors = tk.StringVar()

        label = ttk.Label(self, text="Prisijungimas", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)
        button1 = ttk.Button(self, text="Pradinis",
                             command=lambda: controller.show_frame(StartPage.StartPage))
        button1.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(self, textvariable=self.errors).grid(row=1, column=2)
        ttk.Label(self, text='El. pastas:').grid(row=2, column=1, padx=5, pady=5)
        ttk.Entry(self, textvariable=self.email).grid(row=3, column=1, padx=10, pady=10)
        ttk.Label(self, text='Slaptazodis:').grid(row=4, column=1, padx=5, pady=5)
        ttk.Entry(self, textvariable=self.password, show="*").grid(row=5, column=1, padx=10, pady=10)
        ttk.Button(self, text='Prisijungti', command=self.submit_form).grid(row=6, column=1, padx=10, pady=10)

    def submit_form(self):
        self.errors.set('')
        if self.email != '' and self.password != '':
            email = self.email.get()
            password = self.password.get()
            self.email.set('')
            self.password.set('')

            r = requests.post(
                'http://localhost:8080/OBD-server/api.php?action=login',
                {
                    'email': email,
                    'password': password
                }
            ).json()
            if r['success']:
                self.controller.login(email, r['user_id'])
                self.controller.show_frame(StartPage.StartPage)
            else:
                self.errors.set('Neteisingi prisijungimo duomenys.')
