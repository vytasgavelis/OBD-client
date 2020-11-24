import obd
import tkinter as tk
from tkinter import ttk
import Parameters

LARGEFONT = ("Verdana", 35)

class Gauge(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.command = None
        self.connection = None
        self.parameter_value = tk.StringVar()
        self.parameter_value.set('')

        label = ttk.Label(self, text="Gauge", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)
        ttk.Label(self, textvariable=self.parameter_value).grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Parametrai",
                             command=lambda: self.go_to_parameter_frame(controller))
        button2.grid(row=2, column=1, padx=10, pady=10)

    def set_parameter(self, parameter):
        command = None
        if parameter == 'SPEED':
            command = obd.commands.SPEED
        if parameter == 'RPM':
            command = obd.commands.RPM
        if parameter == 'THROTTLE_POS':
            command = obd.commands.THROTTLE_POS

        self.command = command

    def set_connection(self, connection):
        self.connection = connection

    def show_parameter(self, response):
        self.parameter_value.set(response.value)

    def start(self):
        self.connection.watch(self.command, callback=self.show_parameter)
        self.connection.start()

    def go_to_parameter_frame(self, controller):
        self.connection.stop()
        controller.show_frame(Parameters.Parameters)

