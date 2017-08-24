import sys
from PyQt5 import QtWidgets as widgets


def main():
    # Create application. This manages the top level event loop
    app = widgets.QApplication(sys.argv)

    # Create a new plain widget. Widgets are the base of pretty much all visual components of Qt
    hello = widgets.QWidget()

    # Set a window title on our widget
    hello.setWindowTitle('Hello World')

    # Make our window visible. New widgets are hidden by default
    hello.show()

    # Start the application event loop. This will not return until the application is ready to exit.
    # i.e. when the top level widget is destroyed or we explicitly tell it to
    app.exec_()


if __name__ == '__main__':
    main()
