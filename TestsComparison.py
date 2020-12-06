import tkinter as tk
from tkinter import ttk
import UserTests
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

LARGEFONT = ("Verdana", 35)

class TestsComparison(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button2 = ttk.Button(self, text="Grizti",
                             command=lambda: controller.show_user_tests(UserTests.UserTests))
        button2.grid(row=1, column=1, padx=10, pady=10)

    def start(self, current_user_test, other_user_test):
        figure = plt.Figure(figsize=(5, 4))
        ax = figure.add_subplot(111)
        ax.plot(current_user_test.speed_data)
        ax.plot(current_user_test.maf_data)
        ax.plot(current_user_test.intake_data)
        ax.set_title('Jusu testas')

        canvas = FigureCanvasTkAgg(figure, self)
        canvas.get_tk_widget().grid(row=2, column=1)
        ttk.Label(self, text='Jusu laikas: ' + str(current_user_test.time) + 's').grid(row=3, column=1)

        figure2 = plt.Figure(figsize=(5, 4))
        ax2 = figure2.add_subplot(111)
        ax2.plot(other_user_test.speed_data)
        ax2.plot(other_user_test.maf_data)
        ax2.plot(other_user_test.intake_data)
        ax2.set_title('Kito vartotojo testas')

        canvas2 = FigureCanvasTkAgg(figure2, self)
        canvas2.get_tk_widget().grid(row=2, column=2)
        ttk.Label(self, text='Kito vartotojo laikas: ' + str(other_user_test.time) + 's').grid(row=3, column=2)


