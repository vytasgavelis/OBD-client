import tkinter as tk
from tkinter import ttk
import StartPage
import Gauge
import Graph
from PIL import Image
from PIL import ImageTk

LARGEFONT = ("Verdana", 35)

class Parameters(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg="#ECECEC")

        gauge_image_temp = Image.open('assets/speedometer.png')
        gauge_image_temp = gauge_image_temp.resize((50, 50), Image.ANTIALIAS)
        self.gauge_image = ImageTk.PhotoImage(gauge_image_temp)
        graph_image_temp = Image.open('assets/graph.png')
        graph_image_temp = graph_image_temp.resize((50, 50), Image.ANTIALIAS)
        self.graph_image = ImageTk.PhotoImage(graph_image_temp)
        self.logo_image = tk.PhotoImage(file='assets/parameters.png')

        label = ttk.Label(self, image=self.logo_image)
        label.grid(row=0, column=1, columnspan=3, padx=10, pady=10)

        button1 = ttk.Button(self, text="Pradinis",
                    command=lambda: controller.show_frame(StartPage.StartPage))
        button1.grid(row=1, column=2, padx=10, pady=10)

        ttk.Button(self, text="Apsukos                            ", image=self.gauge_image, compound='left',
                   command=lambda: controller.show_parameter(Gauge.Gauge, 'RPM')
        ).grid(row=2, column=1, padx=10, pady=10)
        ttk.Button(self, text="Apsukos                            ", image=self.graph_image, compound='left',
                   command=lambda: controller.show_parameter(Graph.Graph, 'RPM')
                   ).grid(row=2, column=3, padx=10, pady=10)

        ttk.Button(self, text="Dabartinis greitis              ", image=self.gauge_image, compound='left',
                   command=lambda: controller.show_parameter(Gauge.Gauge, 'SPEED')
        ).grid(row=3, column=1, padx=10, pady=10)
        ttk.Button(self, text="Dabartinis greitis              ", image=self.graph_image, compound='left',
                   command=lambda: controller.show_parameter(Graph.Graph, 'SPEED')
                   ).grid(row=3, column=3, padx=10, pady=10)

        ttk.Button(self, text="Gazo sklende                    ", image=self.gauge_image, compound='left',
                   command=lambda: controller.show_parameter(Gauge.Gauge, 'THROTTLE_POS')
        ).grid(row=4, column=1, padx=10, pady=10)
        ttk.Button(self, text="Gazo sklende                    ", image=self.graph_image, compound='left',
                   command=lambda: controller.show_parameter(Graph.Graph, 'THROTTLE_POS')
                   ).grid(row=4, column=3, padx=10, pady=10)

        ttk.Button(self, text="Kuras                                   ", image=self.gauge_image, compound='left',
                   command=lambda: controller.show_parameter(Gauge.Gauge, 'FUEL_PRESSURE')
        ).grid(row=5, column=1, padx=10, pady=10)
        ttk.Button(self, text="Kuras                                   ", image=self.graph_image, compound='left',
                   command=lambda: controller.show_parameter(Graph.Graph, 'RPM')
                   ).grid(row=5, column=3, padx=10, pady=10)

        ttk.Button(self, text="Isiurbiamo oro kiekis           ", image=self.gauge_image, compound='left',
                   command=lambda: controller.show_parameter(Gauge.Gauge, 'MAF')
        ).grid(row=6, column=1, padx=10, pady=10)
        ttk.Button(self, text="Isiurbiamo oro kiekis           ", image=self.graph_image, compound='left',
                   command=lambda: controller.show_parameter(Graph.Graph, 'MAF')
                   ).grid(row=6, column=3, padx=10, pady=10)

        ttk.Button(self, text="Isiurbiamo oro temperatura", image=self.gauge_image, compound='left',
                   command=lambda: controller.show_parameter(Gauge.Gauge, 'INTAKE_TEMP')
        ).grid(row=7, column=1, padx=10, pady=10)
        ttk.Button(self, text="Isiurbiamo oro temperatura", image=self.graph_image, compound='left',
                   command=lambda: controller.show_parameter(Graph.Graph, 'INTAKE_TEMP')
                   ).grid(row=7, column=3, padx=10, pady=10)
