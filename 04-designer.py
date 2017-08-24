import os
import sys
from  PyQt5 import QtWidgets as widgets
from PyQt5 import uic

# Compute the path to the UI file created by Qt Designer.
# This is an XML file describing the interface
ui_file = os.path.join(os.path.dirname(__file__), '04-numpad.ui')


class NumPadWidget(widgets.QWidget):
    def __init__(self):
        super().__init__()
        # Parse the UI file and add all the elements in the file to self
        uic.loadUi(ui_file, self)

        # Elements we created in Qt Desinger are now available by their names as attributes of self
        print(self.num0_button)


def main():
    app = widgets.QApplication(sys.argv)
    numpad = NumPadWidget()
    numpad.show()
    app.exec_()


if __name__ == '__main__':
    main()
