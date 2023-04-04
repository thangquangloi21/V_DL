from PyQt5.QtWidgets import QPushButton, QFrame
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize
from View.MainView.main_window import MainWindow

SIZE = 40
DISTANCE_BTN = 14


class TabBar(QFrame):
    closeEv: QPushButton = None
    maximizedEv: QPushButton = None
    minximizedEv: QPushButton = None

    def __init__(self, parent, main_window):
        QFrame.__init__(self, parent=parent)
        self.main_window: MainWindow = main_window
        self.setup_window()
        self.setup_view()
        self.setup_event()
        self.max_re = 0

    def setup_window(self):
        self.setMinimumSize(QSize(150, 95))
        self.display_stylesheet()

    def setup_view(self):
        self.setup_close()
        self.setup_maximized()
        self.setup_minimized()

    def setup_close(self):
        self.closeEv = QPushButton(parent=self)
        self.closeEv.resize(SIZE, SIZE)
        self.closeEv.move(2 * (SIZE + DISTANCE_BTN), 0)

        iconClose = QIcon()
        iconClose.addPixmap(QPixmap("./Resource/Icon/icon_close.png"), QIcon.Normal, QIcon.Off)
        self.closeEv.setIcon(iconClose)
        self.closeEv.setIconSize(QSize(SIZE, SIZE))

    def setup_maximized(self):
        self.maximizedEv = QPushButton(parent=self)
        self.maximizedEv.resize(SIZE, SIZE)
        self.maximizedEv.move(SIZE + DISTANCE_BTN, 0)

        iconMax = QIcon()
        iconMax.addPixmap(QPixmap("./Resource/Icon/icon_maximize.png"), QIcon.Normal, QIcon.Off)
        self.maximizedEv.setIcon(iconMax)
        self.maximizedEv.setIconSize(QSize(SIZE, SIZE))

    def setup_minimized(self):
        self.minximizedEv = QPushButton(parent=self)
        self.minximizedEv.resize(SIZE, SIZE)
        self.minximizedEv.move(0, 0)

        iconMin = QIcon()
        iconMin.addPixmap(QPixmap("./Resource/Icon/icon_minimize.png"), QIcon.Normal, QIcon.Off)
        self.minximizedEv.setIcon(iconMin)
        self.minximizedEv.setIconSize(QSize(SIZE, SIZE))

    def setup_event(self):
        self.closeEv.clicked.connect(self.close_event)
        self.minximizedEv.clicked.connect(self.minximized_event)
        self.maximizedEv.clicked.connect(self.maximized_event)

    def close_event(self):
        self.main_window.close()

    def minximized_event(self):
        self.main_window.showMinimized()

    def maximized_event(self):
        if self.max_re == 0:
            self.main_window.showMaximized()
            self.max_re = 1
        elif self.max_re == 1:
            self.main_window.showNormal()
            self.max_re = 0

    def display_stylesheet(self):
        self.setStyleSheet("""
            QPushButton{
                background-color: transparent;
            }
            QPushButton:hover{
                background-color: rgb(127, 127, 127);
            }
            QPushButton:pressed{
                background-color: rgb(14, 68, 184);
            }
        """)
