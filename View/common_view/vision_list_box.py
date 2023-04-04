from PyQt5.QtWidgets import QListWidget
from PyQt5.QtCore import QSize


class VisionListWidget(QListWidget):

    def __init__(self, parent, width=300, height=200):
        QListWidget.__init__(self)
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.setStyleSheet("""
            background: white;
        """)

    def setup_view(self):
        return



