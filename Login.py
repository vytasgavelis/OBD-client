import tkinter as tk
from tkinter import ttk
import StartPage

LARGEFONT = ("Verdana", 35)

class Login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.email = tk.StringVar()
        self.password = tk.StringVar()

        button1 = ttk.Button(self, text="Pradinis",
                             command=lambda: controller.show_frame(StartPage.StartPage))
        button1.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(self, text='El. pastas:').grid(row=2, column=1, padx=5, pady=5)
        ttk.Entry(self, textvariable=self.email).grid(row=3, column=1, padx=10, pady=10)
        ttk.Label(self, text='Slaptazodis:').grid(row=4, column=1, padx=5, pady=5)
        ttk.Entry(self, textvariable=self.password, show="*").grid(row=5, column=1, padx=10, pady=10)
        ttk.Button(self, text='Prisijungti', command=self.submit_form).grid(row=6, column=1, padx=10, pady=10)

    def submit_form(self):
        # TODO send login request to API
        if self.email != '' and self.password != '':
            email = self.email.get()
            self.email.set('')
            self.password.set('')
            self.controller.login(email)
            self.controller.show_frame(StartPage.StartPage)

