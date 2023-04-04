from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtCore import QSize


class VisionProgressBar(QProgressBar):
    def __init__(self, parent, width=400, height=30, value=0):
        QProgressBar.__init__(self, parent=parent)
        self.setup_view()
        self.setValue(value)
        self.setMaximumSize(QSize(width, height))

    def setup_view(self):
        return
