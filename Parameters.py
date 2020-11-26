import tkinter as tk
from tkinter import ttk
import StartPage
import Gauge
import Graph

LARGEFONT = ("Verdana", 35)

class Parameters(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Parametrai", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        button1 = ttk.Button(self, text="Pradinis",
                    command=lambda: controller.show_frame(StartPage.StartPage))
        button1.grid(row=1, column=1, padx=10, pady=10)

        ttk.Button(self, text="Apsukos",
                   command=lambda: controller.show_parameter(Gauge.Gauge, 'RPM')
        ).grid(row=2, column=1, padx=10, pady=10)
        ttk.Button(self, text="Apsuku grafikas",
                   command=lambda: controller.show_parameter(Graph.Graph, 'RPM')
                   ).grid(row=2, column=2, padx=10, pady=10)

        ttk.Button(self, text="Dabartinis greitis",
                   command=lambda: controller.show_parameter(Gauge.Gauge, 'SPEED')
        ).grid(row=3, column=1, padx=10, pady=10)
        ttk.Button(self, text="Dabartinio greicio grafikas",
                   command=lambda: controller.show_parameter(Graph.Graph, 'SPEED')
                   ).grid(row=3, column=2, padx=10, pady=10)

        ttk.Button(self, text="Gazo sklende",
                   command=lambda: controller.show_parameter(Gauge.Gauge, 'THROTTLE_POS')
        ).grid(row=4, column=1, padx=10, pady=10)
        ttk.Button(self, text="Gazo sklendes grafikas",
                   command=lambda: controller.show_parameter(Graph.Graph, 'THROTTLE_POS')
                   ).grid(row=4, column=2, padx=10, pady=10)

        ttk.Button(self, text="Kuras",
                   command=lambda: controller.show_parameter(Gauge.Gauge, 'FUEL_PRESSURE')
        ).grid(row=5, column=1, padx=10, pady=10)
        ttk.Button(self, text="Kuro grafikas",
                   command=lambda: controller.show_parameter(Graph.Graph, 'RPM')
                   ).grid(row=5, column=2, padx=10, pady=10)

        ttk.Button(self, text="Oras",
                   command=lambda: controller.show_parameter(Gauge.Gauge, 'MAF')
        ).grid(row=6, column=1, padx=10, pady=10)
        ttk.Button(self, text="Oro grafikas",
                   command=lambda: controller.show_parameter(Graph.Graph, 'MAF')
                   ).grid(row=6, column=2, padx=10, pady=10)

        ttk.Button(self, text="Isiurbiamo oro temperatura",
                   command=lambda: controller.show_parameter(Gauge.Gauge, 'INTAKE_TEMP')
        ).grid(row=7, column=1, padx=10, pady=10)
        ttk.Button(self, text="Isiurbiamo oro grafikas",
                   command=lambda: controller.show_parameter(Graph.Graph, 'INTAKE_TEMP')
                   ).grid(row=7, column=2, padx=10, pady=10)
