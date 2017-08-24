from PyQt5 import QtGui as gui
from PyQt5 import QtWidgets as widgets
from PyQt5 import QtCore as core

from .color_mixer import ColorMixerWidget


# pytest-qt adds a fixture with several useful helpers.
# When using other test runners, see the QTest module included in Qt for this functionality

def test_init(qtbot):
    # Construct an instance of our widget
    mixer = ColorMixerWidget(gui.QColor('#00FF7F'))
    mixer.show()

    # Tells qtbot to take care of cleaning up our widget after the test is done
    qtbot.addWidget(mixer)

    # Test that the sliders got set to the correct initial values
    assert mixer.red_slider.value() == 0
    assert mixer.green_slider.value() == 255
    assert mixer.blue_slider.value() == 127

    # Accessing the color_hex_edit by name
    assert mixer.findChild(widgets.QLineEdit, 'color_hex_edit').text() == '#00FF7F'


def test_change_red(qtbot):
    mixer = ColorMixerWidget(gui.QColor('black'))
    mixer.show()
    qtbot.addWidget(mixer)

    # Pauses execution of the test so we can see an interact with our widget.
    # Tests will continue when we close the widget.
    # Useful for debugging
    # qtbot.stop()

    # Test that our signal gets emitted when the slider is changed.
    with qtbot.waitSignal(mixer.color_changed):
        mixer.red_slider.setValue(127)

    assert mixer.color.name() == gui.QColor('#7F0000').name()
    assert mixer.color_hex_edit.text() == '#7F0000'


# This test simulates key events directly vs. just setting the value of the line edit
def test_change_color_hex(qtbot):
    mixer = ColorMixerWidget(gui.QColor('black'))
    mixer.show()
    qtbot.addWidget(mixer)

    mixer.color_hex_edit.clear()

    # Test that the signal is not emitted until editing is complete
    with qtbot.assertNotEmitted(mixer.color_changed):
        qtbot.keyClicks(mixer.color_hex_edit, '7F01FF')

    # Triggering a return key event should cause the editingFinished that we are connected to
    # to be emitted
    with qtbot.waitSignal(mixer.color_changed):
        qtbot.keyClick(mixer.color_hex_edit, core.Qt.Key_Return)

    assert mixer.red_slider.value() == 127
    assert mixer.green_slider.value() == 1
    assert mixer.blue_slider.value() == 255


def test_change_color_hex_same_value(qtbot):
    mixer = ColorMixerWidget(gui.QColor('#FF00FF'))
    mixer.show()
    qtbot.addWidget(mixer)

    mixer.color_hex_edit.clear()
    qtbot.keyClicks(mixer.color_hex_edit, 'ff00ff')

    with qtbot.assertNotEmitted(mixer.color_changed):
        qtbot.keyClick(mixer.color_hex_edit, core.Qt.Key_Return)
