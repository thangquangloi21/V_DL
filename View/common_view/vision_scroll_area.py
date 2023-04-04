from PyQt5.QtWidgets import QScrollArea
from PyQt5.QtCore import QSize


class VisionScrollArea(QScrollArea):
    def __init__(self, parent, height=620, width=200):
        QScrollArea.__init__(self, parent=parent)
        self.setMaximumSize(QSize(height, width))
        self.setup_view()

    def setup_view(self):

        return
