import tkinter as tk
from tkinter import ttk
import StartPage
from TestModel import TestModel
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

LARGEFONT = ("Verdana", 35)

class TestsComparison(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

    def start(self, user_test, other_user_test):
        figure = plt.Figure(figsize=(5, 4))
        ax = figure.add_subplot(111)
        ax.plot(user_test.speed_data)
        ax.plot(user_test.maf_data)
        ax.plot(user_test.intake_data)
        ax.set_title('Jusu testas')

        canvas = FigureCanvasTkAgg(figure, self)
        canvas.get_tk_widget().grid(row=2, column=1)
        ttk.Label(self, text='Jusu laikas: ' + str(user_test.time) + 's').grid(row=3, column=1)

        figure2 = plt.Figure(figsize=(5, 4))
        ax2 = figure2.add_subplot(111)
        ax2.plot(other_user_test.speed_data)
        ax2.plot(other_user_test.maf_data)
        ax2.plot(other_user_test.intake_data)
        ax2.set_title('Kito vartotojo testas')

        canvas2 = FigureCanvasTkAgg(figure2, self)
        canvas2.get_tk_widget().grid(row=2, column=2)
        ttk.Label(self, text='Kito vartotojo laikas: ' + str(other_user_test.time) + 's').grid(row=3, column=2)


