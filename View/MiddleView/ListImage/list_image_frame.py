from PyQt5.QtWidgets import QFrame, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from View.MiddleView.ListImage.list_img import ListImg


class ListImage(QFrame):
    def __init__(self, parent):
        QFrame.__init__(self, parent=parent)
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.setStyleSheet("""
            background: transparent;
            border-image: None;
        """)
        self.resize(660, 80)

    def setup_view(self):
        self.setup_last_btn()
        self.setup_next_btn()
        # self.setup_list_image()

    def setup_last_btn(self):
        self.last_btn = QPushButton(parent=self)
        icon_last_btn = QIcon()
        icon_last_btn.addPixmap(QPixmap("./Resource/Icon/previous_button.png"), QIcon.Normal, QIcon.Off)
        self.last_btn.setIcon(icon_last_btn)
        self.setStyleSheet("""
            QPushButton{
                background-color: transparent;
                padding: 2px;
            }
            QPushButton:pressed{
                background-color:rgb(255, 118, 39);
            }
        """)
        self.last_btn.resize(60, 80)
        self.last_btn.move(0, 0)

    def setup_list_image(self):
        self.list_img = ListImg(parent=self)
        self.list_img.resize(540, 80)
        self.list_img.move(60, 0)

    def setup_next_btn(self):
        self.next_btn = QPushButton(parent=self)
        icon_next_btn = QIcon()
        icon_next_btn.addPixmap(QPixmap("./Resource/Icon/next_button.png"), QIcon.Normal, QIcon.Off)
        self.next_btn.setIcon(icon_next_btn)

        self.next_btn.resize(60, 80)
        self.next_btn.move(self.width() - 60, 0)
