import sys
import re
import csv
import PyQt5
from PyQt5 import QtWidgets, QtCore
from PyQt5.uic import loadUi

# Global values
mtow = -1.0
tlos_pow = -1
rates = [[None] * 4, [None] * 2, [None], [None], [None] * 2, [None], [None]]
p1_ua = 0
totals = [None] * 7


class Page1(QtWidgets.QMainWindow):

    def __init__(self):
        super(Page1, self).__init__()

        loadUi('ui/FYP_1.ui', self)

        # Labels
        self.input_1_label.setText('MTOW')
        self.input_2_label.setText('TLOS')
        self.input_1.setText('28.75')
        self.input_2.setText('7')

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

        loadUi('ui/FYP_v2_2.ui', self)

        # Labels
        # self.failure_data = dict()
        # self.rates = [[None] * 4, [None] * 2, [None], [None], [None] * 2, [None], [None]]
        # self.totals = [None] * 7
        # self.final_total = 0
        global rates, totals
        rates[0][0] = 1.24 * pow(10, -4)
        rates[0][1] = 7.42 * pow(10, -4)
        rates[0][2] = 8.39 * pow(10, -6)
        rates[0][3] = 7.61 * pow(10, -6)
        rates[1][0] = 6.71 * pow(10, -6)
        rates[1][1] = 2.13 * pow(10, -6)
        rates[2][0] = 6.19 * pow(10, -6)
        rates[3][0] = 5.96 * pow(10, -4)
        rates[4][0] = 4.95 * pow(10, -6)
        rates[4][1] = 4.95 * pow(10, -6)
        rates[5][0] = 8.81 * pow(10, -5)
        rates[6][0] = 2.13 * pow(10, -6)
        totals[0] = sum(rates[0])
        totals[1] = sum(rates[1])
        totals[2] = sum(rates[2])
        totals[3] = sum(rates[3])
        totals[4] = sum(rates[4])
        totals[5] = sum(rates[5])
        totals[6] = sum(rates[6])
        # rate_1_1 = 1.24 * pow(10, -4)
        # rate_1_2 = 7.42 * pow(10, -4)
        # rate_1_3 = 8.39 * pow(10, -6)
        # rate_1_4 = 7.61 * pow(10, -6)
        # total_1 = sum([rate_1_1, rate_1_2, rate_1_3, rate_1_4])
        # rate_2_1 = 6.71 * pow(10, -6)
        # rate_2_2 = 2.13 * pow(10, -6)
        # total_2 = sum([rate_2_1, rate_2_2])
        # rate_3_1 = 6.19 * pow(10, -6)
        # total_3 = sum([rate_3_1])
        # rate_4_1 = 5.96 * pow(10, -4)
        # total_4 = sum([rate_4_1])
        # rate_5_1 = 4.95 * pow(10, -6)
        # rate_5_2 = 4.95 * pow(10, -6)
        # total_5 = sum([rate_5_1, rate_5_2])
        # rate_6_1 = 8.81 * pow(10, -5)
        # total_6 = sum([rate_6_1])
        # rate_7_1 = 2.13 * pow(10, -6)
        # total_7 = sum([rate_7_1])

        # 1
        self.rate_1_label.setText('Power System')
        self.rate_1_1_label.setText('Motor')
        self.rate_1_1.setText(f'{get_scientific_notation(rates[0][0])}')
        self.rate_1_2_label.setText('Battery')
        self.rate_1_2.setText(f'{get_scientific_notation(rates[0][1])}')
        self.rate_1_3_label.setText('Electron Speed Regulator')
        self.rate_1_3.setText(f'{get_scientific_notation(rates[0][2])}')
        self.rate_1_4_label.setText('Throttle')
        self.rate_1_4.setText(f'{get_scientific_notation(rates[0][3])}')
        self.rate_1.setText(f'{get_scientific_notation(totals[0])}')
        # 2
        self.rate_2_label.setText('Flight Control System')
        self.rate_2_1_label.setText('Flight Control System')
        self.rate_2_1.setText(f'{get_scientific_notation(rates[1][0])}')
        self.rate_2_2_label.setText('Altitude Measurement Sensor')
        self.rate_2_2.setText(f'{get_scientific_notation(rates[1][1])}')
        self.rate_2.setText(f'{get_scientific_notation(totals[1])}')
        # 3
        self.rate_3_label.setText('Electrical System')
        self.rate_3_1_label.setText('Navigation System')
        self.rate_3_1.setText(f'{get_scientific_notation(rates[2][0])}')
        self.rate_3.setText(f'{get_scientific_notation(totals[2])}')
        # 4
        self.rate_4_label.setText('Communication System')
        self.rate_4_1_label.setText('Communication Link')
        self.rate_4_1.setText(f'{get_scientific_notation(rates[3][0])}')
        self.rate_4.setText(f'{get_scientific_notation(totals[3])}')
        # 5
        self.rate_5_label.setText('Frame')
        self.rate_5_1_label.setText('Arm')
        self.rate_5_1.setText(f'{get_scientific_notation(rates[4][0])}')
        self.rate_5_2_label.setText('Rotor')
        self.rate_5_2.setText(f'{get_scientific_notation(rates[4][1])}')
        self.rate_5.setText(f'{get_scientific_notation(totals[4])}')
        # 6
        self.rate_6_label.setText('Cargo Holds')
        self.rate_6_1_label.setText('Cargo Holds')
        self.rate_6_1.setText(f'{get_scientific_notation(rates[5][0])}')
        self.rate_6.setText(f'{get_scientific_notation(totals[5])}')
        # 7
        self.rate_7_label.setText('Ground Support System')
        self.rate_7_1_label.setText('Remote Control')
        self.rate_7_1.setText(f'{get_scientific_notation(rates[6][0])}')
        self.rate_7.setText(f'{get_scientific_notation(totals[6])}')

        # Total
        global p1_ua
        p1_ua = sum(totals)
        self.input_1.setText(f'{get_scientific_notation(p1_ua)}')

        # Buttons
        self.enter_button.clicked.connect(self.calculate)
        self.next_button.clicked.connect(go_next)
        self.back_button.clicked.connect(go_previous)

        self.show()

    def calculate(self):
        print('Calculating...')
        inputs = [
            [self.rate_1_1, self.mtbf_1_1, 0, 0],
            [self.rate_1_2, self.mtbf_1_2, 0, 1],
            [self.rate_1_3, self.mtbf_1_3, 0, 2],
            [self.rate_1_4, self.mtbf_1_4, 0, 3],
            [self.rate_2_1, self.mtbf_2_1, 1, 0],
            [self.rate_2_2, self.mtbf_2_2, 1, 1],
            [self.rate_3_1, self.mtbf_3_1, 2, 0],
            [self.rate_4_1, self.mtbf_4_1, 3, 0],
            [self.rate_5_1, self.mtbf_5_1, 4, 0],
            [self.rate_5_2, self.mtbf_5_2, 4, 1],
            [self.rate_6_1, self.mtbf_6_1, 5, 0],
            [self.rate_7_1, self.mtbf_7_1, 6, 0],
        ]
        try:
            for row in inputs:
                if not row[1].text() == '':
                    rates[row[2]][row[3]] = 1/float(row[1].text())
                    row[0].setText(get_scientific_notation(rates[row[2]][row[3]]))

            # Power
            # total_1 = float(self.rate_1_1.text()) + float(self.rate_1_2.text()) + float(self.rate_1_3.text()) + float(self.rate_1_4.text())
            totals[0] = sum(rates[0])
            self.rate_1.setText(get_scientific_notation(totals[0]))

            # FCS
            # total_2 = float(self.rate_2_1.text()) + float(self.rate_2_2.text())
            totals[1] = sum(rates[1])
            self.rate_2.setText(get_scientific_notation(totals[1]))

            #
            # total_3 = float(self.rate_3_1.text())
            totals[2] = sum(rates[2])
            self.rate_3.setText(get_scientific_notation(totals[2]))

            # total_4 = float(self.rate_4_1.text())
            totals[3] = sum(rates[3])
            self.rate_4.setText(get_scientific_notation(totals[3]))

            # total_5 = float(self.rate_5_1.text()) + float(self.rate_5_2.text())
            totals[4] = sum(rates[4])
            self.rate_5.setText(get_scientific_notation(totals[4]))
            #
            # total_6 = float(self.rate_6_1.text())
            totals[5] = sum(rates[5])
            self.rate_6.setText(get_scientific_notation(totals[5]))

            # total_7 = float(self.rate_7_1.text())
            totals[6] = sum(rates[6])
            self.rate_7.setText(get_scientific_notation(totals[6]))

            p1_ua = sum(totals)
            self.input_1.setText(get_scientific_notation(p1_ua))

            self.next_button.setEnabled(True)

        except ValueError:
            self.next_button.setEnabled(False)
            print('Value error')


class Page3(QtWidgets.QMainWindow):

    def __init__(self):
        super(Page3, self).__init__()

        loadUi('ui/FYP_3.ui', self)

        self.places_label.setText("Where are you flying?")

        # Populate dropdown menu
        with open('Data/TotalSZData.csv', newline='') as f:
            places = csv.reader(f, delimiter=',', quotechar='|')
            next(places)            # Skip header
            names = []
            for row in places:
                names.append(row[2])

        names.sort()
        for name in names:
            self.places_dropdown.addItem(name)

        self.enter_button.clicked.connect(self.check_place)
        self.back_button.clicked.connect(go_previous)

    def check_place(self):
        chosen = self.places_dropdown.currentText()
        print(f'Chosen place is {chosen}')
        population = 0.0
        area = 0.0

        with open('Data/subzone_geo.csv', newline='') as f:
            data = csv.reader(f, delimiter=',', quotechar='|')
            next(data)              # Skip header
            for row in data:
                if row[1] == chosen:
                    if row[4]:
                        print(f'{row[1]} area: {row[3]}')
                        self.place_message_label.setText(f'{row[1]} area: {row[3]}')
                        area = float(row[3])
                    else:
                        print(f'{row[1]} does not have area data.')
                        self.place_message_label.setText(f'{row[1]} population: {row[3]}')
                        return

        with open('Data/TotalSZData.csv', newline='') as f:
            data = csv.reader(f, delimiter=',', quotechar='|')
            next(data)        # Skip header
            for row in data:
                if row[2] == chosen:
                    if row[4]:
                        print(f'{row[2]} population: {row[4]}')
                        current_text = self.place_message_label.text()
                        self.place_message_label.setText(f'{current_text}\n{row[2]} population: {row[4]}')
                        population = float(row[4])
                    else:
                        print(f'{row[2]} does not have population data.')
                        self.place_message_label.setText(f'{row[2]} does not have population data.')
                        return

        # P1_subzone: failure rate = TLOS/(P2/P3)
        # P2 = Crash Area * Population Density * Sheltering Factor
        global mtow, tlos_pow
        p2 = (mtow * 0.220464) * (population/area)
        print(f'p2 = ({mtow} * 0.220464) * ({population}/{area})')
        # P3 = 1
        tlos = pow(10, (tlos_pow))
        print(f'{tlos = }, {tlos_pow}')
        p1_subzone = tlos / (p2 * 1)
        success = p1_ua < p1_subzone
        success_message = 'Can fly ' if success else 'Cannot fly'

        self.mtow_label.setText(f'MTOW: {get_scientific_notation(mtow)}')
        self.tlos_label.setText(f'TLOS: {get_scientific_notation(tlos)}')
        self.p1_subzone_label.setText(f'P1_subzone: {get_scientific_notation(p1_subzone)}')
        self.p1_ua_label.setText(f'P1_UA: {get_scientific_notation(p1_ua)}')
        self.success_message_label.setText(f'P1_UA < P1_subzone: {success}\n{success_message}')

        print(f'{p1_subzone =  }, {get_scientific_notation(p1_subzone)}')
        print(f'{p1_ua =  }, {get_scientific_notation(p1_ua)}')
        print(f'P1_UA < P1_subzone: {success}')


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
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    page_1 = Page1()
    page_2 = Page2()
    page_3 = Page3()
    widget.addWidget(page_1)
    widget.addWidget(page_2)
    widget.addWidget(page_3)
    widget.setFixedSize(1000, 1000)
    widget.show()
    app.exec()
