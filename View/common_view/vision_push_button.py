from PyQt5.QtWidgets import QPushButton, QColorDialog
from PyQt5.QtCore import QSize
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, pyqtSignal


class VisionPushButton(QPushButton):
    def __init__(self, parent, width=300, height=30, text=""):
        QPushButton.__init__(self, parent=parent)
        self.setup_view()
        self.setText(text)
        self.setMaximumSize(QSize(width, height))

    def setup_view(self):
        self.setStyleSheet("""
            QPushButton{
                 background:rgb(255, 55, 55);
                    border-top-left-radius:6px;
                    border-bottom-left-radius:6px;
                    border-top-right-radius:6px;
                    border-bottom-right-radius:6px;
                    border-image:None;
                    border: 5px;
            }
            QPushButton:hover{
                color: white;
                font-weight: bold;
                font: 15px;                                
                background: orange;
            }
            QPushButton:pressed{
                background: rgb(204, 68, 184);
            }
        """)
        return


class VisionColorPushButton(VisionPushButton):
    color: QColorDialog = None

    def __init__(self, parent, *args, color=None, **kwargs):
        VisionPushButton.__init__(self, parent=parent, *args, **kwargs)
        self.color = None
        self._default = color
        self.pressed.connect(self.setup_color)
        self.set_color(self._default)

    def setup_color(self):
        dlg = QColorDialog()
        if self.color:
            dlg.setCurrentColor(QColor(self.color))

        if dlg.exec_():
            self.set_color(dlg.currentColor().name())

    def set_color(self, color):
        if color != self.color:
            self.color = color
            # self.color_changed.emit(color)

        if self.color:
            self.setStyleSheet("background-color: %s;" % self.color)
        else:
            self.setStyleSheet("")

