"""
Written by Kim Maglalang - Polyspawn https://www.youtube.com/channel/UCoP753pwrAjK6P3gcmZAHAw
A PySide2 UI example. The tool will create spheres, animate them, and playblast.
Written for Python 3 and Maya 2020 and beyond.
"""
import random
import re
import os
from maya import cmds
from maya import mel
from maya import OpenMayaUI as omui
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from shiboken2 import wrapInstance
global First_UI

class FirstToolUI(QWidget):

    def __init__(self, parent=None):
        super(FirstToolUI, self).__init__(parent)
        object_name = "FirstToolUI_uniqueId"
        title = "First UI Tool"
        # Close previously opened
        if cmds.window(object_name, title=title, exists=True):
            cmds.deleteUI(object_name)
            
        self.setWindowFlags(Qt.Window)

        # Set the object name     
        self.setObjectName(object_name)

        # Customize some window values
        self.setWindowTitle("First UI Tool")
        self.setGeometry(50, 50, 250, 150)

        # Add widgets to your window
        self.build_ui()
        self.connect_ui()

    def build_ui(self):
        """Populate the window with widgets."""
        vertical_layout = QVBoxLayout()
        self.setLayout(vertical_layout)
        self.sphere_button = QPushButton(text="Create Sphere", parent=self)
        self.animate_button = QPushButton(text="Animate All Spheres", parent=self)
        self.playblast_button = QPushButton(text="Playblast", parent=self)
        vertical_layout.addWidget(self.sphere_button)
        vertical_layout.addWidget(self.animate_button)
        vertical_layout.addWidget(self.playblast_button)

    def connect_ui(self):
        """Connect widgets to actions."""
        self.sphere_button.clicked.connect(self.create_action)
        self.animate_button.clicked.connect(self.animate_action)
        self.playblast_button.clicked.connect(self.playblast_action)

    def create_action(self):
        print("Creating Sphere")
        cmds.polySphere(r=1, sx=20, sy=20, ax=[0, 1, 0], cuv=2, ch=1)

    def animate_action(self):
        print("Animating Sphere")

        sphere_list = cmds.ls("pSphere*", transforms=1)

        for t in [0, 50, 100]:
            for node in sphere_list:
                cmds.setKeyframe(node, at="translateX", v=random.randint(-10, 10), t=t)
                cmds.setKeyframe(node, at="translateY", v=random.randint(-10, 10), t=t)
                cmds.setKeyframe(node, at="translateZ", v=random.randint(-10, 10), t=t)

    def playblast_action(self):
        print("Playblasting")

        filename = "sphere_playblast_v001.avi"
        dir = "D:/YOUTUBE/2022/polyspawn/your first maya tool/playblast"
        output_file = "%s/%s" % (dir, filename)

        # Auto-Version up if using v###.ext
        contents = os.listdir(dir)
        if filename in contents:
            r = re.compile(".*v\d{3}.avi")
            series_list = list(filter(r.match, contents))
            occupied_versions = [re.search(r"v\d{3}", x).group(0) for x in series_list]
            occupied_ints = [int(x.split("v")[-1]) for x in occupied_versions]
            new_version = "v%03d" % (max(occupied_ints)+1)
            new_filename = "%s%s.avi" % (filename.split("v")[0], new_version)
            output_file = "%s/%s" % (dir, new_filename)


        # Playblast
        cmds.playblast(
           format="avi",
           filename=output_file,
           sequenceTime=0,
           clearCache=1,
           viewer=2,
           showOrnaments=1,
           fp=4,
           percent=50,
           compression="none",
           quality=70,
        )

def get_main_window():
    """Get the maya window pointer to parent this tool under."""
    omui.MQtUtil.mainWindow()
    ptr = omui.MQtUtil.mainWindow()
    # for Py3 use int() , for Py2 use long() , more info: https://docs.python.org/3/whatsnew/3.0.html#integers
    maya_window_widget = wrapInstance(int(ptr), QWidget)
    return maya_window_widget

maya_window_widget = get_main_window()
try:
    First_UI.close()
except NameError:
    pass
First_UI = FirstToolUI(maya_window_widget)
First_UI.show()
