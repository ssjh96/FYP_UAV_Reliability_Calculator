import sys
import re
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

        loadUi('ui/FYP_2.ui', self),

        # Labels


        # Values
        self.sub_rates = dict()
        self.comp_rates = dict()
        self.sub_mtbf = dict()
        self.comp_mtbf = dict()

        # Buttons
        self.enter_button.clicked.connect(self.calculate)

        self.show()

    def calculate(self):
        print('Calculating...')
        try:
            self.sub_rates[1] = float(self.rate_1.text())
            self.sub_rates[2] = float(self.rate_2.text())
            self.sub_rates[3] = float(self.rate_3.text())
            self.sub_rates[4] = float(self.rate_4.text())
            self.sub_rates[5] = float(self.rate_5.text())
            self.sub_rates[6] = float(self.rate_6.text())
            self.sub_rates[7] = float(self.rate_7.text())

            for value in self.sub_rates.values():
                if value <= 0:
                    raise ValueError

            self.input_1.setText(str(sum(self.sub_rates.values())))

        except ValueError:
            self.next_button.setEnabled(False)
            print('Value error')

def go_next():
    widget.setCurrentIndex(widget.currentIndex() + 1)


def go_previous():
    widget.setCurrentIndex(widget.currentIndex() - 1)


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
