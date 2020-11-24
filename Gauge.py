import obd
import tkinter as tk
from tkinter import ttk
import Parameters
import tk_tools

LARGEFONT = ("Verdana", 35)

class Gauge(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.connection = None

        button2 = ttk.Button(self, text="Parametrai",
                             command=lambda: self.go_to_parameter_frame(controller))
        button2.grid(row=2, column=1, padx=10, pady=10)

    def draw_gauge(self, max_value, label, unit):
        self.rs = tk_tools.Gauge(self, max_value=max_value, label=label, unit=unit)
        self.rs.grid(row=0, column=0, padx=10, pady=10)
        self.rs.set_value(0)

    def show_parameter(self, response):
        self.rs.set_value(float(format(float(str(response.value).split()[0]), '.2f')))

    def start(self, connection, parameter):
        command = None
        max_gauge_value = 1
        label = ''
        unit = ''
        if parameter == 'SPEED':
            command = obd.commands.SPEED
            max_gauge_value = 300
            label = 'Greitis'
            unit = 'km/h'
        if parameter == 'RPM':
            command = obd.commands.RPM
            max_gauge_value = 9000
            label = 'Apsukos'
            unit = 'rpm'
        if parameter == 'THROTTLE_POS':
            command = obd.commands.THROTTLE_POS
            max_gauge_value = 100
            label = 'Gazo sklendes pozicija'
            unit = '%'
        if parameter == 'FUEL_PRESSURE':
            command = obd.commands.FUEL_PRESSURE
            max_gauge_value = 300
            label = 'Kuro slegis'
            unit = 'PSI'
        if parameter == 'MAF':
            command = obd.commands.MAF
            max_gauge_value = 300
            label = 'Oro srauto kiekis oro matuokleje'
            unit = 'kg/s'
        if parameter == 'INTAKE_TEMP':
            command = obd.commands.INTAKE_TEMP
            max_gauge_value = 300
            label = 'Oro temperatura isiurbimo kolektoriuje'
            unit = '°C'

        self.draw_gauge(max_gauge_value, label, unit)
        self.connection = connection
        connection.watch(command, callback=self.show_parameter)
        connection.start()

    def go_to_parameter_frame(self, controller):
        self.connection.stop()
        controller.show_frame(Parameters.Parameters)
