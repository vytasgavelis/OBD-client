import tkinter as tk
from tkinter import ttk
import StartPage

LARGEFONT = ("Verdana", 35)

class Profile(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Profilis", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        button2 = ttk.Button(self, text="Pradinis",
                             command=lambda: controller.show_frame(StartPage.StartPage))
        button2.grid(row=2, column=1, padx=10, pady=10)