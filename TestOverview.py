import tkinter as tk
from tkinter import ttk
import UserTests
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class TestOverview(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg="#ECECEC")

        self.tests_image = tk.PhotoImage(file='assets/tests.png')
        label = ttk.Label(self, image=self.tests_image)
        label.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

        button2 = ttk.Button(self, text="Atgal",
                             command=lambda: controller.show_user_tests(UserTests.UserTests))
        button2.grid(row=2, column=1, padx=10, pady=10)

    def start(self, test):
        figure = plt.Figure(figsize=(5, 4))
        figure.patch.set_facecolor('#ECECEC')
        ax = figure.add_subplot(111)
        ax.plot(test.speed_data, label='Greitis(km/h)')
        ax.plot(test.maf_data, label='Oro srautas(kg/s)')
        ax.plot(test.intake_data, label='Isiurbiamo oro temperatura(°C)')
        ax.set_title('Testas #' + str(test.test_id))

        ax.legend(title='Parametrai:', loc='upper left', fontsize='x-small')

        canvas = FigureCanvasTkAgg(figure, self)
        canvas.get_tk_widget().grid(row=3, column=1)
        ttk.Label(self, text='Laikas: ' + format(float(test.time), '.2f') + 's').grid(row=4, column=1)
        ttk.Label(self, text='Greitis: ' + str(test.target_speed) + ' km/h').grid(row=5, column=1)
