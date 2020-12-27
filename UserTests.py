import tkinter as tk
from tkinter import ttk
import Tests
import requests
import json
from TestModel import TestModel
import TestOverview

class UserTests(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.tests = []
        self.controller = controller

        self.tests_box = ttk.Combobox(self)
        self.configure(bg="#ECECEC")

        self.tests_image = tk.PhotoImage(file='assets/tests.png')
        label = ttk.Label(self, image=self.tests_image)
        label.grid(row=1, column=1, padx=10, pady=10)

        button2 = ttk.Button(self, text="Atgal",
                             command=lambda: controller.show_frame(Tests.Tests))
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

    def start(self, user_id):
        tests = self.get_user_tests(user_id)
        self.tests = tests

        tests_options = []
        for test in tests:
            tests_options.append('#' + str(test.test_id) + ' Laikas: ' + format(float(test.time), '.2f') + 's')
        self.tests_box['values'] = tests_options
        if len(tests_options) > 0:
            self.tests_box.set(tests_options[0])
        self.tests_box.state(["readonly"])
        self.tests_box.grid(row=3, column=1, padx=10, pady=10)

        ttk.Button(self, text="Rodyti",
                    command=lambda: self.on_show_button_click()).grid(row=4, column=1)

    def get_test_by_id(self, tests, id):
        for test in tests:
            if str(test.test_id) == str(id):
                return test

        return None

    def on_show_button_click(self):
        test = self.get_test_by_id(self.tests, self.tests_box.get()[1])
        self.controller.show_test(TestOverview.TestOverview, test)
