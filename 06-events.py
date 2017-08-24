import sys
from PyQt5 import QtWidgets as widgets
from PyQt5 import QtGui as gui
from PyQt5 import QtCore as core


class ExampleWidget(widgets.QWidget):
    def __init__(self):
        super().__init__()
        self.lines = []
        self.line_start = None
        self.line_end = None

    # Override QWidget's mouse button press handling.
    # Called whenever a mouse button is pressed while the pointer is over this widget
    def mousePressEvent(self, event):
        self.line_start = event.pos()

    def mouseMoveEvent(self, event):
        if self.line_start:
            self.line_end = event.pos()

            # Tell the widget it needs to be re-drawn
            self.update()

    def mouseReleaseEvent(self, event):
        self.lines.append(core.QLineF(self.line_start, self.line_end))
        self.line_start = self.line_end = None

        self.update()

    # Called whenever a key is pressed while this widget is in focus
    def keyPressEvent(self, event):
        if event.key() in (core.Qt.Key_Delete, core.Qt.Key_Backspace):
            self.lines = []
            self.update()

    # A somewhat special event that is sent whenever Qt needs to redraw this widget.
    # We can override this event handler to draw anything we want in the widget.
    # This is not necessary to do for the vast majority of use cases
    def paintEvent(self, event):
        super().paintEvent(event)

        # A QPainter does our drawing
        painter = gui.QPainter(self)
        pen = gui.QPen()
        pen.setWidth(5)
        painter.setPen(pen)
        painter.drawLines(self.lines)

        if self.line_start and self.line_end:
            painter.drawLine(self.line_start, self.line_end)


def main():
    app = widgets.QApplication(sys.argv)
    example = ExampleWidget()
    example.show()
    app.exec_()


if __name__ == '__main__':
    main()
