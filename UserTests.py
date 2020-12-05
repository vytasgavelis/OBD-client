import tkinter as tk
from tkinter import ttk
import StartPage
from TestModel import TestModel
import TestsComparison

LARGEFONT = ("Verdana", 35)

class UserTests(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = ttk.Label(self, text="Jusu testai", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        button2 = ttk.Button(self, text="Pradinis",
                             command=lambda: controller.show_frame(StartPage.StartPage))
        button2.grid(row=2, column=1, padx=10, pady=10)

        self.user_tests_box = ttk.Combobox(self)
        user_tests_options = []
        self.user_tests = self.get_user_tests(5)
        for test in self.user_tests:
            user_tests_options.append('#' + str(test.test_id) + ' Laikas: ' + str(test.time) + 's')
        self.user_tests_box['values'] = user_tests_options
        self.user_tests_box.set(user_tests_options[0])
        self.user_tests_box.state(["readonly"])
        self.user_tests_box.grid(row=3, column=1, padx=10, pady=10)

        self.other_user_tests_box = ttk.Combobox(self)
        other_user_tests_options = []
        self.other_user_tests = self.get_other_user_tests()
        for test in self.other_user_tests:
            other_user_tests_options.append('#' + str(test.test_id) + ' Laikas: ' + str(test.time) + 's')
        self.other_user_tests_box['values'] = other_user_tests_options
        self.other_user_tests_box.set(other_user_tests_options[0])
        self.other_user_tests_box.state(["readonly"])
        self.other_user_tests_box.grid(row=3, column=3, padx=10, pady=10)

        ttk.Button(self, text="Lyginti",
                   command=lambda: self.on_compare_button_click()).grid(row=3, column=2, padx=10, pady=10)

    def get_user_tests(self, user_id):
        # TODO fetch tests from server
        speed_data = range(1, 100, 10)
        maf_data = [50, 60, 70, 30, 30, 70, 70, 80, 120, 130]
        intake_data = [20, 20, 30, 30, 40, 50, 60, 90, 100, 100]
        tests = []
        for i in range(1, 5):
            tests.append(TestModel(
                test_id = i,
                test_type = '0-100',
                target_speed = '100',
                time = i * 5,
                speed_data = speed_data,
                maf_data = maf_data,
                intake_data = intake_data
            ))

        return tests

    def get_other_user_tests(self):
        # TODO fetch tests from server
        speed_data = range(1, 100, 10)
        maf_data = [50, 60, 70, 30, 30, 70, 70, 80, 120, 130]
        intake_data = [20, 20, 30, 30, 40, 50, 60, 90, 100, 100]
        tests = []
        for i in range(1, 5):
            tests.append(TestModel(
                test_id=i,
                test_type='0-100',
                target_speed='100',
                time=i * 5,
                speed_data=speed_data,
                maf_data=maf_data,
                intake_data=intake_data
            ))

        return tests

    def get_test_by_id(self, tests, id):
        for test in tests:
            if str(test.test_id) == str(id):
                return test

        return None

    def on_compare_button_click(self):
        user_test = self.get_test_by_id(self.user_tests, self.user_tests_box.get()[1])
        other_user_test = self.get_test_by_id(self.other_user_tests, self.other_user_tests_box.get()[1])
        self.controller.show_tests_comparison(TestsComparison.TestsComparison, user_test, other_user_test)


