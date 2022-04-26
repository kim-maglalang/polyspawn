"""
Written by Kim Maglalang - Polyspawn https://www.youtube.com/channel/UCoP753pwrAjK6P3gcmZAHAw
A PySide2 UI template to running your first UI in Maya.
Written for Python 3 and Maya 2020 and beyond.
"""
from maya import OpenMayaUI as omui
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance


class FirstToolUI(QWidget):

    def __init__(self, parent=None):
        super(FirstToolUI, self).__init__(parent)

        self.setWindowFlags(Qt.Window)

        # Set the object name     
        self.setObjectName('FirstToolUI_uniqueId')

        # Customize some window values
        self.setWindowTitle('First UI Tool')
        self.setGeometry(50, 50, 250, 150)

        # Add widgets to your window
        self.build_ui()
        self.connect_ui()

    def build_ui(self):
        pass

    def connect_ui(self):
        pass

    def action(self):
        pass

def get_main_window():
    """Get the maya window pointer to parent this tool under."""
    omui.MQtUtil.mainWindow()
    ptr = omui.MQtUtil.mainWindow()
    # for Py3 use int() , for Py2 use long() , more info: https://docs.python.org/3/whatsnew/3.0.html#integers
    maya_window_widget = wrapInstance(int(ptr), QWidget)
    return maya_window_widget

maya_window_widget = get_main_window()
tool = FirstToolUI(maya_window_widget)
tool.show()