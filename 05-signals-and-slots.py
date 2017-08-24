import os
import sys
from PyQt5 import QtWidgets as widgets
from PyQt5 import uic


ui_file = os.path.join(os.path.dirname(__file__), '05-signals-and-slots.ui')


class ExampleWidget(widgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):
        uic.loadUi(ui_file, self)

        # Connect the `clicked` signal from the QButton to the `on_button_clicked` slot
        # Whenever the click_me_button emits the `clicked` signal, `ok_button_clicked` will
        #  automatically be called
        self.click_me_button.clicked.connect(self.on_button_clicked)

        # Connect the `textChanged` signal from the QLineEdit to the `say_hello` slot
        # This signal includes an argument for updated text in the line edit so the slot will be
        # called with a string argument
        self.hello_line_edit.textChanged.connect(self.say_hello)

        # Connect the `valueChanged` signal from the QSlider to the `setValue` slot on the QProgressBar
        # Both the signal and the slot support an int argument so we can connect them directly
        self.progress_slider.valueChanged.connect(self.progress_bar.setValue)

    def on_button_clicked(self):
        # Display a simple dialog. Execution will pause here until the user dismisses the dialog
        widgets.QMessageBox.information(self, 'Hello', 'You clicked the button')

    def say_hello(self, name):
        name = name.strip()
        if not name:
            name = 'World'

        # Update the label text
        hello_text = 'Hello, {}'.format(name)
        self.hello_label.setText(hello_text)


def main():
    app = widgets.QApplication(sys.argv)
    example = ExampleWidget()
    example.show()
    app.exec_()


if __name__ == '__main__':
    main()
