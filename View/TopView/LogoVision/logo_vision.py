from PyQt5.QtWidgets import QLabel, QSizePolicy
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap


class LogoVision(QLabel):
    sizePolicy: QSizePolicy

    def __init__(self, parent):
        QLabel.__init__(self, parent=parent)
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.setPixmap(QPixmap("./Resource/Icon/logo.png").scaled(120, 120))
        self.setMaximumSize(QSize(120, 95))
        self.sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.setSizePolicy(self.sizePolicy)

    def setup_view(self):
        return
