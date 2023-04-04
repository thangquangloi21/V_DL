from PyQt5.QtWidgets import QFrame, QSizePolicy
from PyQt5.QtCore import QSize


class VisionFrame(QFrame):
    sizePolicy: QSizePolicy = None

    def __init__(self, parent):
        QFrame.__init__(self, parent=parent)
        self.setup_vieww()
        self.sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.setSizePolicy(self.sizePolicy)

    def setup_vieww(self):
        self.setStyleSheet("""
            QFrame{
                border: None;
                background: rgb(100, 100, 100);
                color: white;
            }
        """)


