from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QPushButton
from PyQt5.QtGui import QIcon, QPixmap
from View.Setting.light.left_groupbox import LeftGroupbox
from View.Setting.light.right_groupbox import RightGroupbox
from View.common_view.thanh_tieu_de import ThanhTieuDe
from View.MainView.main_window import MainWindow
from PyQt5.QtGui import QMouseEvent
SPACERW = 20
SPACERH = 20


class LightForm(QMainWindow):
    left_groupbox: LeftGroupbox = None
    right_groupbox: RightGroupbox = None
    save_btn: QPushButton = None
    thanh_tieu_de: ThanhTieuDe

    def __init__(self, main_window):
        QMainWindow.__init__(self)
        self.main_window: MainWindow = main_window
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setup_window()
        self.setup_view()
        self.show()

    def setup_window(self):
        self.setFixedSize(570, 520)
        self.setObjectName("Setting Camera")
        self.setStyleSheet("""
            QMainWindow{
                background: rgb(150, 150, 150);
            }
            QGroupBox {
                color: black;
                font: 15px;
                font-weight: bold;
                background-color:transparent;
                border: 2px solid gray;
                border-radius: 5px;
                margin-top: 1ex; /* leave space at the top for the title */
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 0px 0px 0px;
                border-image: None;
            }
            QLabel{
                color: black;
                font: 15px;
            }
            QPushButton{
                background: grey;
                font: 15px;
                font-weight: bold;
            }
            QPushButton:hover{
                background-color: rgb(127, 127, 127);
            }
            QPushButton:pressed{
                background-color: rgb(14, 68, 184);
            }
        """)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

    def setup_view(self):
        self.setup_thanh_tieu_de()
        self.setup_left_combobox()
        self.setup_right_combobox()
        self.setup_btn()

    def setup_thanh_tieu_de(self):
        self.thanh_tieu_de = ThanhTieuDe(parent=self, width=self.width(), height=40, name_window="Light Setting")
        self.thanh_tieu_de.resize(self.width(), 40)
        self.thanh_tieu_de.move(0, 0)
        return

    def setup_left_combobox(self):
        self.left_groupbox = LeftGroupbox(parent=self, main_window=self.main_window)
        self.left_groupbox.resize(220, 400)
        self.left_groupbox.move(SPACERW, 2 * SPACERH + 20)
        return

    def setup_right_combobox(self):
        self.right_groupbox = RightGroupbox(parent=self, main_window=self.main_window)
        self.right_groupbox.resize(300, 400)
        self.right_groupbox.move(12.5 * SPACERW, 2 * SPACERH + 20)
        return

    def setup_btn(self):
        self.save_btn = QPushButton(parent=self, text="Save")
        self.save_btn.resize(90, 40)
        self.save_btn.move(11.5 * SPACERW, 22.5 * SPACERH + 20)
        return

       # Kéo di Chuyển app

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.startPos = event.pos()

    def mouseReleaseEvent(self, a0: QMouseEvent) -> None:
        # todo reset position
        self.startPos = None
        return

    def mouseMoveEvent(self, event):
        try:
            if self.startPos is None:
                return
            if self.startPos.x() <= self.thanh_tieu_de.width\
                    and self.startPos.y() <= self.thanh_tieu_de.height \
                    and not self.isMaximized():
                self.move(self.pos() + (event.pos() - self.startPos))
        except Exception as error:
            print(error)