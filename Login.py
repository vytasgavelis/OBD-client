import tkinter as tk
from tkinter import ttk
import StartPage
import requests
from tkinter import messagebox

LARGEFONT = ("Verdana", 35)
MEDIUMFONT = ("Verdana", 25)

class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg="#ECECEC")

        self.controller = controller
        self.email = tk.StringVar()
        self.password = tk.StringVar()

        self.logo_image = tk.PhotoImage(file='assets/header.png')
        ttk.Label(self, image=self.logo_image).grid(row=0, column=0, padx=10, pady=10)

        label = ttk.Label(self, text="Prisijungimas", font=MEDIUMFONT)
        label.grid(row=1, column=0, padx=10, pady=10)
        button1 = ttk.Button(self, text="Pradinis",
                             command=lambda: controller.show_frame(StartPage.StartPage))
        button1.grid(row=2, column=0, padx=10, pady=10)

        ttk.Label(self, text='El. pastas:').grid(row=3, column=0, padx=5, pady=5)
        ttk.Entry(self, textvariable=self.email).grid(row=4, column=0, padx=10, pady=10)
        ttk.Label(self, text='Slaptazodis:').grid(row=5, column=0, padx=5, pady=5)
        ttk.Entry(self, textvariable=self.password, show="*").grid(row=6, column=0, padx=10, pady=10)
        ttk.Button(self, text='Prisijungti', command=self.submit_form).grid(row=7, column=0, padx=10, pady=10)

    def submit_form(self):
        if self.email != '' and self.password != '':
            email = self.email.get()
            password = self.password.get()
            self.email.set('')
            self.password.set('')

            try:
                r = requests.post(
                    'http://localhost:8080/OBD-server/api.php?action=login',
                    {
                        'email': email,
                        'password': password
                    },
                    timeout=3
                ).json()
                if r['success']:
                    self.controller.login(email, r['user_id'])
                    self.controller.show_frame(StartPage.StartPage)
                else:
                    messagebox.showerror('Klaida', 'Neteisingi prisijungimo duomenys.')

            except requests.exceptions.RequestException:
                messagebox.showerror('Klaida', 'Tinklo klaida')
