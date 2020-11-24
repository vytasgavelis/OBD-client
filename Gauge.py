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

    def draw_gauge(self, max_value):
        self.rs = tk_tools.RotaryScale(self, max_value=max_value)
        self.rs.grid(row=0, column=0, padx=10, pady=10)
        self.rs.set_value(0)

    def show_parameter(self, response):
        self.rs.set_value(float(str(response.value).split()[0]))

    def start(self, connection, parameter):
        command = None
        max_gauge_value = 1
        if parameter == 'SPEED':
            command = obd.commands.SPEED
            max_gauge_value = 300
        if parameter == 'RPM':
            command = obd.commands.RPM
            max_gauge_value = 9000
        if parameter == 'THROTTLE_POS':
            command = obd.commands.THROTTLE_POS
            max_gauge_value = 100

        self.draw_gauge(max_gauge_value)
        self.connection = connection
        connection.watch(command, callback=self.show_parameter)
        connection.start()

    def go_to_parameter_frame(self, controller):
        self.connection.stop()
        controller.show_frame(Parameters.Parameters)
