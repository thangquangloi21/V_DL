from PyQt5.QtWidgets import QFrame, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize

WIDGHT = 104
HEIGHT = 80
SPACE = 5


class ListImg(QFrame):

    def __init__(self, parent):
        QFrame.__init__(self, parent=parent)
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.setStyleSheet("""
            QFrame{
                background: transparent;
                border-image: None;
            }
            QPushButton{
                background-color: transparent;
                padding: 2px;
            }
            QPushButton:pressed{
                background-color:grey;
            }
        """)
        self.resize(540, 80)

    def setup_view(self):
        self.setup_img1()
        self.setup_img2()
        self.setup_img3()
        self.setup_img4()
        self.setup_img5()

    def setup_img1(self):
        self.img1 = QPushButton(parent=self)
        self.img1.setIcon(QIcon(QPixmap("./Resource/Icon/fgdfg.png")))
        self.img1.setIconSize(QSize(WIDGHT * 2, HEIGHT * 2))
        self.img1.resize(WIDGHT, HEIGHT)
        self.img1.move(0, 0)
        self.img1.clicked.connect(self.clicks)

    def clicks(self):
        print("Show Image")

    def setup_img2(self):
        self.img2 = QPushButton(parent=self)
        self.img2.setIcon(QIcon(QPixmap("./Resource/Icon/fgdfg.png")))
        self.img2.setIconSize(QSize(WIDGHT * 2, HEIGHT * 2))
        self.img2.resize(WIDGHT, HEIGHT)
        self.img2.clicked.connect(self.clicks)
        self.img2.move(WIDGHT + SPACE, 0)

    def setup_img3(self):
        self.img3 = QPushButton(parent=self)
        self.img3.setIcon(QIcon(QPixmap("./Resource/Icon/fgdfg.png")))
        self.img3.setIconSize(QSize(WIDGHT * 2, HEIGHT * 2))
        self.img3.resize(WIDGHT, HEIGHT)
        self.img3.clicked.connect(self.clicks)
        self.img3.move(2 * (WIDGHT + SPACE), 0)

    def setup_img4(self):
        self.img4 = QPushButton(parent=self)
        self.img4.setIcon(QIcon(QPixmap("./Resource/Icon/fgdfg.png")))
        self.img4.setIconSize(QSize(WIDGHT * 2, HEIGHT * 2))
        self.img4.resize(WIDGHT, HEIGHT)
        self.img4.clicked.connect(self.clicks)
        self.img4.move(3 * (WIDGHT + SPACE), 0)

    def setup_img5(self):
        self.img5 = QPushButton(parent=self)
        self.img5.setIcon(QIcon(QPixmap("./Resource/Icon/fgdfg.png")))
        self.img5.setIconSize(QSize(WIDGHT * 2, HEIGHT * 2))
        self.img5.resize(WIDGHT, HEIGHT)
        self.img5.clicked.connect(self.clicks)
        self.img5.move(4 * (WIDGHT + SPACE), 0)
