import tkinter as tk
from tkinter import ttk
import StartPage

LARGEFONT = ("Verdana", 35)

class Parameters(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Parametrai", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="StartPage",
                             command=lambda: controller.show_frame(StartPage.StartPage))
        button1.grid(row=1, column=1, padx=10, pady=10)