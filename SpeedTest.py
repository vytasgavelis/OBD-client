import tkinter as tk
from tkinter import ttk
import Tests
import time
import obd

LARGEFONT = ("Verdana", 35)

class SpeedTest(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.started = False
        self.connection = False
        self.start_time = 0
        self.elapsed_time = tk.StringVar(value=0)
        self.speed = tk.StringVar(value=0)
        self.target_speed = 100
        self.test_text = tk.StringVar(value='Pradeti')

        label = ttk.Label(self, text="Greicio testas", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)
        button2 = ttk.Button(self, text="Testai",
                             command=lambda: self.go_to_tests_frame(controller))
        button2.grid(row=2, column=1, padx=10, pady=10)

        ttk.Button(self, textvariable=self.test_text,
                   command=lambda: self.start_test()).grid(row=3, column=1)

        ttk.Label(self, textvariable=self.elapsed_time).grid(row=4, column=1, padx=10, pady=10)
        ttk.Label(self, textvariable=self.speed).grid(row=5, column=1, padx=10, pady=10)

    def show_parameter(self, response):
        self.elapsed_time.set(time.time() - self.start_time)
        self.speed.set(float(format(float(str(response.value).split()[0]), '.2f')))

    def start_test(self):
        if not self.started:
            self.started = True
            self.test_text.set('Restartuoti')
            self.start_time = time.time()
            self.connection.start()
        else:
            self.started = False
            self.test_text.set('Pradeti')
            self.start_time = 0
            self.elapsed_time.set(0)
            self.connection.stop()


    def start(self, connection, parameter):
        command = None
        if parameter == 'SPEED':
            command = obd.commands.SPEED
        if parameter == 'RPM':
            command = obd.commands.RPM
        if parameter == 'THROTTLE_POS':
            command = obd.commands.THROTTLE_POS
        if parameter == 'FUEL_PRESSURE':
            command = obd.commands.FUEL_PRESSURE
        if parameter == 'MAF':
            command = obd.commands.MAF
        if parameter == 'INTAKE_TEMP':
            command = obd.commands.INTAKE_TEMP

        self.connection = connection
        self.connection.watch(command, callback=self.show_parameter)

    def go_to_tests_frame(self, controller):
        self.start_time = 0
        self.elapsed_time.set(0)
        self.connection.stop()
        controller.show_frame(Tests.Tests)
