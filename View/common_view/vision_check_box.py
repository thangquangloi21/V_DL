from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtCore import QSize


class VisionCheckBox(QCheckBox):

    def __init__(self, parent, width=30, height=30):
        QCheckBox.__init__(self, parent=parent)
        self.setup_view()
        self.setMaximumSize(QSize(width, height))

    def setup_view(self):
        return

