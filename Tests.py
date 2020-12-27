import tkinter as tk
from tkinter import ttk
import StartPage
import SpeedTest
import UserTests

LARGEFONT = ("Verdana", 35)

class Tests(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg="#ECECEC")

        self.tests_image = tk.PhotoImage(file='assets/tests.png')
        self.test1_image = tk.PhotoImage(file='assets/0-60.png')
        self.test2_image = tk.PhotoImage(file='assets/0-100.png')
        self.user_tests_image = tk.PhotoImage(file='assets/user_tests.png')
        self.compare_tests_image = tk.PhotoImage(file='assets/compare_test.png')

        ttk.Label(self, image=self.tests_image).grid(row=1, column=1, columnspan=3, padx=10, pady=10)

        button2 = ttk.Button(self, text="Atgal",
                             command=lambda: controller.show_frame(StartPage.StartPage))
        button2.grid(row=2, column=2, padx=10, pady=10)

        self.speed_test2_button = tk.Button(self, image=self.test1_image,
                                             command=lambda: controller.show_parameter(SpeedTest.SpeedTest, 'SPEED'))
        self.speed_test2_button.grid(row=3, column=1, padx=10, pady=10)
        self.speed_test2_button['state'] = tk.DISABLED

        self.speed_test1_button = tk.Button(self, image=self.test2_image,
                             command=lambda: controller.show_parameter(SpeedTest.SpeedTest, 'SPEED'))
        self.speed_test1_button.grid(row=4, column=1, padx=10, pady=10)
        self.speed_test1_button['state'] = tk.DISABLED

        self.user_tests_button = tk.Button(self, image=self.user_tests_image)
        self.user_tests_button['state'] = tk.DISABLED
        self.user_tests_button.grid(row=3, column=3, padx=10, pady=10)

        self.compare_tests_button = tk.Button(self, image=self.compare_tests_image,
                             command=lambda: controller.show_user_tests(UserTests.UserTests))
        self.compare_tests_button['state'] = tk.DISABLED
        self.compare_tests_button.grid(row=4, column=3, padx=10, pady=10)
