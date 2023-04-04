from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QSize


class VisionLabel(QLabel):
    def __init__(self, width=100, height=30, text=""):
        QLabel.__init__(self)
        self.setup_view()
        self.setText(text)
        self.setMaximumSize(QSize(width, height))

    def setup_view(self):
        self.setStyleSheet("""
            background: transparent;
            color:white;
            font:14px;
            border-image: None;
        }
        """)
        return

    def red_color(self):
        self.setStyleSheet("font:14px; color: red; font-weight: bold;")

    def green_color(self):
        self.setStyleSheet("font:14px; color: green; font-weight: bold;")

        # self.get_connected_btn.setCursor(QCursor(Qt.PointingHandCursor))