from PyQt5.QtWidgets import QGroupBox, QSizePolicy
from PyQt5.QtCore import QSize
# error


class VisionGroupBox(QGroupBox):
    sizePolicy: QSizePolicy = None

    def __init__(self, parent):
        QGroupBox.__init__(self, parent=parent)
        self.setup_view()

    def setup_view(self):
        self.setStyleSheet("""
            QGroupBox {
                background: transparent;
                color: white;
                font: 18px;
                font-weight: bold;
                background-color:transparent;
                border: 2px solid gray;
                border-radius: 5px;
                margin-top: 1ex; /* leave space at the top for the title */
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 0px 0px 0px; 
                border-image: None;
            }
        """)


