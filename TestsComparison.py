import tkinter as tk
from tkinter import ttk
import UserTests
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

LARGEFONT = ("Verdana", 35)

class TestsComparison(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg="#ECECEC")

        self.tests_image = tk.PhotoImage(file='assets/tests.png')
        label = ttk.Label(self, image=self.tests_image)
        label.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

        button2 = ttk.Button(self, text="Atgal",
                             command=lambda: controller.show_user_tests(UserTests.UserTests))
        button2.grid(row=2, column=2, padx=10, pady=10)

    def start(self, current_user_test, other_user_test):
        figure = plt.Figure(figsize=(5, 4))
        figure.patch.set_facecolor('#ECECEC')
        ax = figure.add_subplot(111)
        ax.plot(current_user_test.speed_data, label='Greitis(km/h)')
        ax.plot(current_user_test.maf_data, label='Oro srautas(kg/s)')
        ax.plot(current_user_test.intake_data, label='Isiurbiamo oro temperatura(°C)')
        ax.set_title('Testas #' + str(current_user_test.test_id))

        ax.legend(title='Parametrai:', loc='upper left', fontsize='x-small')

        canvas = FigureCanvasTkAgg(figure, self)
        canvas.get_tk_widget().grid(row=3, column=1)
        ttk.Label(self, text='Laikas: ' + format(float(current_user_test.time), '.2f') + 's').grid(row=4, column=1)

        figure2 = plt.Figure(figsize=(5, 4))
        figure2.patch.set_facecolor('#ECECEC')
        ax2 = figure2.add_subplot(111)
        ax2.plot(other_user_test.speed_data, label='Greitis(km/h)')
        ax2.plot(other_user_test.maf_data, label='Oro srautas(kg/s)')
        ax2.plot(other_user_test.intake_data, label='Isiurbiamo oro temperatura(°C)')
        ax2.set_title('Testas #' + str(other_user_test.test_id))

        ax2.legend(title='Parametrai:', loc='upper left', fontsize='x-small')

        canvas2 = FigureCanvasTkAgg(figure2, self)
        canvas2.get_tk_widget().grid(row=3, column=3)
        ttk.Label(self, text='Laikas: ' + format(float(other_user_test.time), '.2f') + 's').grid(row=4, column=3)


