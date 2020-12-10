import tkinter as tk
from tkinter import ttk
import StartPage
from TestModel import TestModel
import TestsComparison
import requests
import json

LARGEFONT = ("Verdana", 35)

class UserTests(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.current_user_tests = []
        self.other_user_tests = []

        self.user_tests_box = ttk.Combobox(self)
        self.other_user_tests_box = ttk.Combobox(self)

        label = ttk.Label(self, text="Jusu testai", font=LARGEFONT)
        label.grid(row=0, column=4, padx=10, pady=10)

        button2 = ttk.Button(self, text="Pradinis",
                             command=lambda: controller.show_frame(StartPage.StartPage))
        button2.grid(row=2, column=1, padx=10, pady=10)

    def get_user_tests(self, user_id):
        r = requests.get('http://localhost:8080/OBD-server/api.php?action=get_tests&user_id=' + str(user_id)).json()
        tests = []

        if r['success']:
            for test in r['speed_tests']:
                data = json.loads(test['test_data'])
                tests.append(TestModel(
                    test_id=int(test['test_id']),
                    test_type=data['type'],
                    target_speed=data['target_speed'],
                    time=data['time'],
                    speed_data=data['speed_data'],
                    maf_data=data['maf_data'],
                    intake_data=data['intake_data']
                ))

        return tests

    def get_all_tests(self):
        r = requests.get('http://localhost:8080/OBD-server/api.php?action=get_tests').json()
        tests = []

        if r['success']:
            for test in r['speed_tests']:
                data = json.loads(test['test_data'])
                tests.append(TestModel(
                    test_id=int(test['test_id']),
                    test_type=data['type'],
                    target_speed=data['target_speed'],
                    time=data['time'],
                    speed_data=data['speed_data'],
                    maf_data=data['maf_data'],
                    intake_data=data['intake_data']
                ))

        return tests

    def start(self, user_id):
        current_user_tests = self.get_user_tests(user_id)
        self.current_user_tests = current_user_tests
        other_user_tests = self.get_all_tests()
        self.other_user_tests = other_user_tests
        self.draw_tests_boxes(current_user_tests, other_user_tests)

    def get_test_by_id(self, tests, id):
        for test in tests:
            if str(test.test_id) == str(id):
                return test

        return None

    def on_compare_button_click(self):
        user_test = self.get_test_by_id(self.current_user_tests, self.user_tests_box.get()[1])
        other_user_test = self.get_test_by_id(self.other_user_tests, self.other_user_tests_box.get()[1])
        self.controller.show_tests_comparison(TestsComparison.TestsComparison, user_test, other_user_test)

    def draw_tests_boxes(self, current_user_tests, other_user_tests):
        user_tests_options = []
        for test in current_user_tests:
            user_tests_options.append('#' + str(test.test_id) + ' Laikas: ' + str(test.time) + 's')
        self.user_tests_box['values'] = user_tests_options
        self.user_tests_box.set(user_tests_options[0])
        self.user_tests_box.state(["readonly"])
        self.user_tests_box.grid(row=3, column=1, padx=10, pady=10)

        other_user_tests_options = []
        for test in other_user_tests:
            other_user_tests_options.append('#' + str(test.test_id) + ' Laikas: ' + str(test.time) + 's')
        self.other_user_tests_box['values'] = other_user_tests_options
        self.other_user_tests_box.set(other_user_tests_options[0])
        self.other_user_tests_box.state(["readonly"])
        self.other_user_tests_box.grid(row=3, column=3, padx=10, pady=10)

        ttk.Button(self, text="Lyginti",
                   command=lambda: self.on_compare_button_click()).grid(row=3, column=2, padx=10, pady=10)
