import sys
import re
import csv
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi

# Global values
mtow = -1.0
tlos_pow = -1


class Page1(QtWidgets.QMainWindow):

    def __init__(self):
        super(Page1, self).__init__()

        loadUi('ui/FYP_1.ui', self)

        # Labels
        self.input_1_label.setText('<<< Input 1 label here >>>')
        self.input_2_label.setText('<<< Input 2 label here >>>')

        # Buttons
        self.next_button.setEnabled(False)
        self.enter_button.clicked.connect(self.enter)
        self.next_button.clicked.connect(go_next)

        self.show()

    def enter(self):
        try:
            input_1 = float(self.input_1.text())
            input_2 = int(self.input_2.text())

            # Throw error if any values are less than 0 (must be positive)
            if input_1 <= 0 and input_2 <= 0:
                raise ValueError

            global mtow
            mtow = input_1
            global tlos_pow
            tlos_pow = input_2 * -1         # Convert to negative

            print(f'{mtow = }')
            print(f'{tlos_pow = }')

            self.next_button.setEnabled(True)
            # self.error_message.setText('')

        except ValueError:
            self.next_button.setEnabled(False)
            print('Value error')
            # self.error_message.setText('Error...')
            return


class Page2(QtWidgets.QMainWindow):

    def __init__(self):
        super(Page2, self).__init__()

        loadUi('ui/FYP_v2_2.ui', self),

        # Labels
        self.failure_data = dict()
        rate_1_1 = 1.24 * pow(10, -4)
        rate_1_2 = 7.42 * pow(10, -4)
        rate_1_3 = 8.39 * pow(10, -6)
        rate_1_4 = 7.61 * pow(10, -6)
        total_1 = sum([rate_1_1, rate_1_2, rate_1_3, rate_1_4])
        rate_2_1 = 6.71 * pow(10, -6)
        rate_2_2 = 2.13 * pow(10, -6)
        total_2 = sum([rate_2_1, rate_2_2])
        rate_3_1 = 6.19 * pow(10, -6)
        total_3 = sum([rate_3_1])
        rate_4_1 = 5.96 * pow(10, -4)
        total_4 = sum([rate_4_1])
        rate_5_1 = 4.95 * pow(10, -6)
        rate_5_2 = 4.95 * pow(10, -6)
        total_5 = sum([rate_5_1, rate_5_2])
        rate_6_1 = 8.81 * pow(10, -5)
        total_6 = sum([rate_6_1])
        rate_7_1 = 2.13 * pow(10, -6)
        total_7 = sum([rate_7_1])

        # 1
        self.rate_1_label.setText('Power System')
        self.rate_1_1_label.setText('Motor')
        self.rate_1_1.setText(f'{rate_1_1:.1e}')
        self.rate_1_2_label.setText('Battery')
        self.rate_1_2.setText(f'{rate_1_2:.1e}')
        self.rate_1_3_label.setText('Electron Speed Regulator')
        self.rate_1_3.setText(f'{rate_1_3:.1e}')
        self.rate_1_4_label.setText('Throttle')
        self.rate_1_4.setText(f'{rate_1_4:.1e}')
        self.rate_1.setText(f'{total_1:.1e}')
        # 2
        self.rate_2_label.setText('Flight Control System')
        self.rate_2_1_label.setText('Flight Control System')
        self.rate_2_1.setText(f'{rate_2_1:.1e}')
        self.rate_2_2_label.setText('Altitude Measurement Sensor')
        self.rate_2_2.setText(f'{rate_2_2:.1e}')
        self.rate_2.setText(f'{total_2:.1e}')
        # 3
        self.rate_3_label.setText('Electrical System')
        self.rate_3_1_label.setText('Navigation System')
        self.rate_3_1.setText(f'{rate_3_1:.1e}')
        self.rate_3.setText(f'{total_3:.1e}')
        # 4
        self.rate_4_label.setText('Communication System')
        self.rate_4_1_label.setText('Communication Link')
        self.rate_4_1.setText(f'{rate_4_1:.1e}')
        self.rate_4.setText(f'{total_4:.1e}')
        # 5
        self.rate_5_label.setText('Frame')
        self.rate_5_1_label.setText('Arm')
        self.rate_5_1.setText(f'{rate_5_1:.1e}')
        self.rate_5_2_label.setText('Rotor')
        self.rate_5_2.setText(f'{rate_5_2:.1e}')
        self.rate_5.setText(f'{total_5:.1e}')
        # 6
        self.rate_6_label.setText('Cargo Holds')
        self.rate_6_1_label.setText('Cargo Holds')
        self.rate_6_1.setText(f'{rate_6_1:.1e}')
        self.rate_6.setText(f'{total_6:.1e}')
        # 7
        self.rate_7_label.setText('Ground Support System')
        self.rate_7_1_label.setText('Remote Control')
        self.rate_7_1.setText(f'{rate_7_1:.1e}')
        self.rate_7.setText(f'{total_7:.1e}')

        # Total
        total = sum([total_1, total_2, total_3, total_4, total_5, total_6, total_7])
        self.input_1.setText(f'{total:.1e}')

        # Values
        self.sub_rates = dict()
        self.comp_rates = dict()
        self.sub_mtbf = dict()
        self.comp_mtbf = dict()

        # Buttons
        self.enter_button.clicked.connect(self.calculate)

        print(self.failure_data)
        self.show()

    def calculate(self):
        print('Calculating...')
        inputs = [
            [self.rate_1_1, self.mtbf_1_1],
            [self.rate_1_2, self.mtbf_1_2],
            [self.rate_1_3, self.mtbf_1_3],
            [self.rate_1_4, self.mtbf_1_4],
            [self.rate_2_1, self.mtbf_2_1],
            [self.rate_2_2, self.mtbf_2_2],
            [self.rate_3_1, self.mtbf_3_1],
            [self.rate_4_1, self.mtbf_4_1],
            [self.rate_5_1, self.mtbf_5_1],
            [self.rate_5_2, self.mtbf_5_2],
            [self.rate_6_1, self.mtbf_6_1],
            [self.rate_7_1, self.mtbf_7_1],
        ]
        try:
            for row in inputs:
                if row[1] != '':
                    new_rate = 1/float(row[1].text())
                    row[0].setText(get_scientific_notation(new_rate))

        except ValueError:
            self.next_button.setEnabled(False)
            print('Value error')


class Page3(QtWidgets.QMainWindow):

    def __init__(self):
        super(Page3, self).__init__()


def go_next():
    widget.setCurrentIndex(widget.currentIndex() + 1)


def go_previous():
    widget.setCurrentIndex(widget.currentIndex() - 1)


def get_scientific_notation(x):
    return f'{x:.1e}'

# def get_float_or_empty(x):
#     if x is '':
#         return ''
#     else if converted := float(x):
#         return converted

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    page_1 = Page1()
    page_2 = Page2()
    widget.addWidget(page_1)
    widget.addWidget(page_2)
    widget.setFixedSize(1000, 1000)
    widget.show()
    app.exec()
