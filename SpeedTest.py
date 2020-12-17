import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import Tests
import time
import obd
import json
import requests
import tk_tools
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

LARGEFONT = ("Verdana", 35)

class SpeedTest(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.started = False
        self.connection = False
        self.start_time = 0
        self.elapsed_time = tk.StringVar(value=0)
        self.speed = tk.StringVar(value=0)
        self.maf_data = []
        self.speed_data = []
        self.intake_data = []

        self.target_speed = 100
        self.test_text = tk.StringVar(value='Pradeti')

        label = ttk.Label(self, text="Greicio testas", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)
        button2 = ttk.Button(self, text="Testai",
                             command=lambda: self.go_to_tests_frame(controller))
        button2.grid(row=2, column=1, padx=10, pady=10)

        ttk.Button(self, textvariable=self.test_text,
                   command=lambda: self.on_test_button_click()).grid(row=3, column=1)

        ttk.Label(self, text='Laikas: ').grid(row=4, column=1)
        ttk.Label(self, textvariable=self.elapsed_time).grid(row=4, column=2, padx=10, pady=10)
        ttk.Label(self, text='Greitis: ').grid(row=5, column=1)
        ttk.Label(self, textvariable=self.speed).grid(row=5, column=2, padx=10, pady=10)

    def process_speed_response(self, response):
        if self.started:
            self.elapsed_time.set(format(time.time() - self.start_time, '.2f'))
            speed = float(format(float(str(response.value).split()[0]), '.2f'))
            self.speed.set(speed)
            self.speed_data.append(speed)
            if speed >= self.target_speed:
                self.started = False
                self.test_text.set('Pradeti')
                self.show_save_dialog()

            self.draw_graph()

    def process_maf_response(self, response):
        if self.started:
            self.maf_data.append(float(format(float(str(response.value).split()[0]), '.2f')))

    def process_intake_response(self, response):
        if self.started:
            self.intake_data.append(float(format(float(str(response.value).split()[0]), '.2f')))

    def on_test_button_click(self):
        if not self.started:
            self.start_test()
        else:
            self.stop_test()

    def start_test(self):
        self.start_time = 0
        self.elapsed_time.set(0)
        self.speed.set(0)
        self.maf_data.clear()
        self.speed_data.clear()
        self.intake_data.clear()
        self.started = True
        self.test_text.set('Restartuoti')
        self.start_time = time.time()

    def stop_test(self):
        self.started = False
        self.test_text.set('Pradeti')
        self.start_time = 0
        self.elapsed_time.set(0)
        self.speed.set(0)

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

        self.draw_graph()
        self.connection = connection
        self.connection.watch(command, callback=self.process_speed_response)
        self.connection.watch(obd.commands.MAF, callback=self.process_maf_response)
        self.connection.watch(obd.commands.INTAKE_TEMP, callback=self.process_intake_response)
        self.connection.start()

    def draw_graph(self):
        try:
            self.canvas.get_tk_widget().pack_forget()
        except AttributeError:
            pass
        figure = plt.Figure(figsize=(5, 4))
        ax = figure.add_subplot(111)
        ax.plot(self.speed_data, label='Greitis(km/h)')
        ax.plot(self.maf_data, label='Oro srautas(kg/s)')
        ax.plot(self.intake_data, label='Isiurbiamo oro temperatura(°C)')

        ax.legend(title='Parametrai:', loc='upper left', fontsize='x-small')

        self.canvas = FigureCanvasTkAgg(figure, self)
        self.canvas.get_tk_widget().grid(row=6, column=1)
        ax.set_title('Testas')

    def show_save_dialog(self):
        if self.controller.is_logged_in():
            should_save = messagebox.askyesno(title='Issaugoti', message='Ar norite issaugoti testa?', icon='question')
            if should_save:
                data = json.dumps({
                    'type': '0-100',
                    'target_speed': self.target_speed,
                    'time': self.elapsed_time.get(),
                    'speed_data': self.speed_data,
                    'maf_data': self.maf_data,
                    'intake_data': self.intake_data
                })
                r = requests.post(
                    'http://localhost:8080/OBD-server/api.php?action=upload_speed_test',
                    {
                        'user_id': self.controller.user_id,
                        'speed_test_data': data
                    }
                ).json()

                if r['success']:
                    messagebox._show('Issaugota', 'Testas sekmingai issaugotas.')
                else:
                    messagebox.showerror('Klaida', 'Nepavyko issaugoti testo.')


    def go_to_tests_frame(self, controller):
        self.start_time = 0
        self.elapsed_time.set(0)
        self.connection.stop()
        controller.show_frame(Tests.Tests)
