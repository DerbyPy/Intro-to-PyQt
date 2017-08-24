import os

import sys
from PyQt5 import QtWidgets as widgets, uic
from PyQt5 import QtGui as gui
from PyQt5 import QtCore as core

ui_file = os.path.join(os.path.dirname(__file__), 'color-mixer.ui')


class ColorMixerWidget(widgets.QWidget):
    # Create a custom signal that other widgets can connect to to be notified when
    # the color has been updated.
    # The signal has one argument that it will pass to any slots that are connected to it
    color_changed = core.pyqtSignal(gui.QColor)

    def __init__(self, starting_color):
        super().__init__()
        self.color = starting_color
        self.setup_ui()

    def setup_ui(self):
        uic.loadUi(ui_file, self)

        # Tell the color_display widget it needs to fill its background
        self.color_display.setAutoFillBackground(True)

        # Connect our signals and slots
        self.color_hex_edit.editingFinished.connect(self.set_hex)

        self.red_slider.valueChanged.connect(self.set_red)
        self.green_slider.valueChanged.connect(self.set_green)
        self.blue_slider.valueChanged.connect(self.set_blue)

        self.update_ui()

    def update_ui(self):
        # Set the background color of the color display widget
        palette = self.color_display.palette()
        palette.setColor(gui.QPalette.Background, self.color)
        self.color_display.setPalette(palette)

        # Set the slider and line edit values so they always stay synced
        self.red_slider.setValue(self.color.red())
        self.green_slider.setValue(self.color.green())
        self.blue_slider.setValue(self.color.blue())

        self.color_hex_edit.setText(self.color.name())

    def set_color(self, color):
        if color == self.color:
            # The color didn't change so we don't need to do anything
            return
        self.color = color
        self.update_ui()

        # Emit our color changed signal, triggering any slots connected to it
        self.color_changed.emit(self.color)

    def set_hex(self):
        color_hex = self.color_hex_edit.text()
        self.set_color(gui.QColor(color_hex))

    def set_red(self, value):
        color = gui.QColor(self.color)
        color.setRed(value)
        self.set_color(color)

    def set_green(self, value):
        color = gui.QColor(self.color)
        color.setGreen(value)
        self.set_color(color)

    def set_blue(self, value):
        color = gui.QColor(self.color)
        color.setBlue(value)
        self.set_color(color)


def main():
    app = widgets.QApplication(sys.argv)
    example = ColorMixerWidget(gui.QColor('gray'))
    example.show()
    app.exec_()


if __name__ == '__main__':
    main()
