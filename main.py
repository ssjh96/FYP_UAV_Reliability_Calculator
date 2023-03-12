import sys
import re
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi

# Global values
mtow = -1.0
tlos = -1


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

            global mtow
            mtow = input_1
            global tlos
            tlos = input_2

            print(f'{mtow = }')
            print(f'{tlos = }')

            self.next_button.setEnabled(True)
            # self.error_message.setText('')

        except ValueError:
            self.next_button.setEnabled(False)
            # self.error_message.setText('Error...')
            return


class Page2(QtWidgets.QMainWindow):

    def __init__(self):
        super(Page2, self).__init__()

        loadUi('ui/FYP_2.ui', self),

        # Labels


        # Buttons


        self.show()


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
