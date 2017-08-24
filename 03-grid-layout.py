import sys
from PyQt5 import QtWidgets as widgets


class NumpadWidget(widgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Create some simple button widgets for the digits 1-9
        buttons = [
            [widgets.QPushButton(str(i)) for i in range(7, 10)],
            [widgets.QPushButton(str(i)) for i in range(4, 7)],
            [widgets.QPushButton(str(i)) for i in range(1, 4)],
        ]

        layout = widgets.QGridLayout()

        for x, row in enumerate(buttons):
            for y, btn in enumerate(row):
                # Add the button to the grid at column x and row y
                layout.addWidget(btn, x, y)

        # add our 0 button centered at the bottom
        layout.addWidget(widgets.QPushButton('0'), 3, 1)

        self.setLayout(layout)

        self.setWindowTitle('Numbers')


def main():
    app = widgets.QApplication(sys.argv)
    numpad = NumpadWidget()
    numpad.show()
    app.exec_()


if __name__ == '__main__':
    main()
