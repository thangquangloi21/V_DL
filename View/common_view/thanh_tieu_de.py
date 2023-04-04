
from PyQt5.QtWidgets import QFrame, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from View.Setting.Commnunication.communication_setting import CommunicationSetting

SIZE_BTN = 35


class ThanhTieuDe(QFrame):
    name_win: QLabel = None
    communication_setting_window: CommunicationSetting = None
    icon_close: QIcon = None
    icon_maximized: QIcon = None
    icon_minimized: QIcon = None
    btn_close: QPushButton = None
    btn_maximized: QPushButton = None
    btn_minimized: QPushButton = None

    def __init__(self, parent, width=200, height=30, name_window=""):
        QFrame.__init__(self, parent=parent)
        self.name_window = name_window
        self.SIZE_BTN = height
        self.communication_setting_window = parent
        self.width = width
        self.height = height
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.resize(self.width, self.height)
        self.setStyleSheet("""
            QFrame{
                background: grey;
            }
            QLabel{
                background: transparent;
                color: black;
                font: 17px;
            }
            QTextEdit{
                background-color: rgb(200, 200, 200);
                border-image: None;
                font: 14px;
                color: black;
            }
            QPushButton{
                background-color: transparent;
                font: 15px;
                font-weight: bold;
            }
            QPushButton:hover{
                background-color: orange;
            }
            QPushButton:pressed{
                background-color: rgb(14, 68, 184);
            }
        """)
        return

    def setup_view(self):
        self.setup_name_window()
        self.setup_btn_close()
        self.setup_btn_maximized()
        self.setup_minimized()

    def setup_name_window(self):
        self.name_win = QLabel(parent=self, text=self.name_window)
        self.name_win.resize(200, 30)
        self.name_win.move(10, 5)
        return

    def setup_btn_close(self):
        self.icon_close = QIcon()
        self.icon_close.addPixmap(QPixmap("./Resource/Icon/icon_close.png"), QIcon.Normal, QIcon.Off)
        self.btn_close = QPushButton(parent=self)
        self.btn_close.resize(SIZE_BTN, self.SIZE_BTN)
        self.btn_close.setIcon(self.icon_close)
        self.btn_close.move(self.width - 1 * SIZE_BTN, 0)
        self.btn_close.clicked.connect(self.click_close_btn)
        return

    def setup_btn_maximized(self):
        self.icon_maximized = QIcon()
        self.icon_maximized.addPixmap(QPixmap("./Resource/Icon/icon_maximize.png"), QIcon.Normal, QIcon.Off)
        self.btn_maximized = QPushButton(parent=self)
        self.btn_maximized.resize(SIZE_BTN, self.SIZE_BTN)
        self.btn_maximized.setIcon(self.icon_maximized)
        self.btn_maximized.move(self.width - 2 * 1 * SIZE_BTN, 0)
        self.btn_maximized.clicked.connect(self.click_maximized_btn)
        return

    def setup_minimized(self):
        self.icon_minimized = QIcon()
        self.icon_minimized.addPixmap(QPixmap("./Resource/Icon/icon_minimize.png"), QIcon.Normal, QIcon.Off)
        self.btn_minimized = QPushButton(parent=self)
        self.btn_minimized.resize(SIZE_BTN, self.SIZE_BTN)
        self.btn_minimized.setIcon(self.icon_minimized)
        self.btn_minimized.move(self.width - 3 * 1 * SIZE_BTN, 0)
        self.btn_minimized.clicked.connect(self.click_minimized_btn)
        return

    def click_close_btn(self):
        self.communication_setting_window.close()

    def click_maximized_btn(self):
        return

    def click_minimized_btn(self):
        self.communication_setting_window.showMinimized()


