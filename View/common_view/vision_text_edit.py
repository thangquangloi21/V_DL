from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtCore import QSize


class VisionTextEdit(QTextEdit):
    def __init__(self, parent, width=250, height=30):
        QTextEdit.__init__(self, parent=parent)
        self.setup_view()
        self.setMaximumSize(QSize(width, height))

    def setup_view(self):
        self.setStyleSheet("""
            QTextEdit{
                border-image: None;
                font: 14px;
                color: white;
            }
        """)
        return
