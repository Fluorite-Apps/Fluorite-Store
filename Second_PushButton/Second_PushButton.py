from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSvgWidgets import *

style = '''
QPushButton {{
    border: none;
    padding-left: 10px;
    padding-right: 5px;
    color: black;
    border-radius: 25;    
    background-color: rgb(194, 234, 189);
}}
QPushButton:hover {{
    background-color: rgb(87, 134, 92);
}}
QPushButton:pressed {{    
    background-color: rgb(87, 109, 84);
}}
'''

class custompushbutton(QPushButton):
    def __init__(
        self,
        text,
        parent = None,
    ):
        super().__init__()

        self.setText(text)
        if parent != None:
            self.setParent(parent)
        self.setCursor(Qt.PointingHandCursor)
