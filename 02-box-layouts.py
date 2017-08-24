import sys
from PyQt5 import QtWidgets as widgets


class HelloWidget(widgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Create a label widget. A label is typically a static element that displays some short text
        hello_label = widgets.QLabel('Hello')
        world_label = widgets.QLabel('World')
        smile_label = widgets.QLabel('\u263a')

        # Create a layout that will arrange our widgets either horizontally or vertically
        layout = widgets.QHBoxLayout()
        # layout = widgets.QVBoxLayout()

        # Add our widgets to the layout
        layout.addWidget(hello_label)
        layout.addWidget(world_label)
        layout.addWidget(smile_label)

        # set this widget's layout. This will add our labels as children on this widget
        self.setLayout(layout)

        self.setWindowTitle('Layouts!!!1!')


def main():
    app = widgets.QApplication(sys.argv)
    hello = HelloWidget()
    hello.show()
    app.exec_()


if __name__ == '__main__':
    main()
