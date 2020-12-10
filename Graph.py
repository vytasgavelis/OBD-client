import obd
import tkinter as tk
from tkinter import ttk
import Parameters
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

LARGEFONT = ("Verdana", 35)

class Graph(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.connection = None
        self.data = []
        self.canvas = None
        self.title = ''
        self.unit = ''

        button2 = ttk.Button(self, text="Parametrai",
                             command=lambda: self.go_to_parameter_frame(controller))
        button2.grid(row=2, column=1, padx=10, pady=10)

    def draw_graph(self):
        try:
            self.canvas.get_tk_widget().pack_forget()
        except AttributeError:
            pass
        figure = plt.Figure(figsize=(5, 4))
        ax = figure.add_subplot(111)
        ax.plot(self.data)

        self.canvas = FigureCanvasTkAgg(figure, self)
        self.canvas.get_tk_widget().grid(row=3, column=1)
        ax.set_title(self.title + ' ' + self.unit)

    def process_response(self, response):
        self.data.append(float(format(float(str(response.value).split()[0]), '.2f')))
        self.draw_graph()

    def start(self, connection, parameter):
        command = None
        max_value = 1
        label = ''
        unit = ''
        if parameter == 'SPEED':
            command = obd.commands.SPEED
            max_value = 300
            label = 'Greitis'
            unit = 'km/h'
        if parameter == 'RPM':
            command = obd.commands.RPM
            max_value = 9000
            label = 'Apsukos'
            unit = 'rpm'
        if parameter == 'THROTTLE_POS':
            command = obd.commands.THROTTLE_POS
            max_value = 100
            label = 'Gazo sklendes pozicija'
            unit = '%'
        if parameter == 'FUEL_PRESSURE':
            command = obd.commands.FUEL_PRESSURE
            max_value = 300
            label = 'Kuro slegis'
            unit = 'PSI'
        if parameter == 'MAF':
            command = obd.commands.MAF
            max_value = 300
            label = 'Oro srauto kiekis oro matuokleje'
            unit = 'kg/s'
        if parameter == 'INTAKE_TEMP':
            command = obd.commands.INTAKE_TEMP
            max_value = 300
            label = 'Oro temperatura isiurbimo kolektoriuje'
            unit = '°C'

        self.connection = connection
        self.title = label
        self.unit = unit
        self.connection.watch(command, callback=self.process_response)
        self.connection.start()

    def go_to_parameter_frame(self, controller):
        try:
            self.canvas.get_tk_widget().pack_forget()
        except AttributeError:
            pass
        self.connection.stop()
        self.data.clear()
        controller.show_frame(Parameters.Parameters)
