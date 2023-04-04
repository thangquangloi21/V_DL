from PyQt5.QtWidgets import QMainWindow, QLabel, QTextEdit, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMouseEvent
from PyQt5 import QtCore
SPACERW = 20
SPACERH = 40


class CommunicationSetting(QMainWindow):
    ip_text_edit: QTextEdit
    port_text_edit: QTextEdit
    save_btn: QPushButton

    def __init__(self, name):
        QMainWindow.__init__(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.startPos = None
        self.name = name
        self.setup_window()
        self.setup_view()
        self.show()

    def setup_window(self):
        # self.resize(600, 500)
        self.setFixedSize(320, 210)
        # hide window hint
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.setObjectName(self.name)
        # self.setStyleSheet("rgb(207, 216, 220")
        self.setStyleSheet("""
            QMainWindow{
                background: rgb(170, 170, 170);
            }
            QLabel{
                color: black;
                font: 15px;
            }
            QTextEdit{
                background-color: rgb(200, 200, 200);
                border-image: None;
                font: 14px;
                color: black;
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

    def setup_view(self):
        self.setup_thanh_tieu_de()
        self.setup_ip_inf()
        self.setup_port_inf()
        self.setup_save_btn()
        return

    def setup_thanh_tieu_de(self):
        from View.common_view.thanh_tieu_de import ThanhTieuDe
        self.thanh_tieu_de = ThanhTieuDe(parent=self, width=self.width(), height=35, name_window=self.name)
        self.thanh_tieu_de.resize(self.width(), 35)
        self.thanh_tieu_de.move(0, 0)
        return

    def setup_ip_inf(self):
        lbl_ip = QLabel(parent=self, text="IP address: ")
        lbl_ip.resize(90, 30)
        lbl_ip.move(SPACERW, 1.3 * SPACERH)

        self.ip_text_edit = QTextEdit(parent=self)
        self.ip_text_edit.resize(190, 30)
        self.ip_text_edit.move(5 * SPACERW, 1.3 * SPACERH)
        return

    def setup_port_inf(self):
        lbl_port = QLabel(parent=self, text="Port:")
        lbl_port.resize(70, 30)
        lbl_port.move(SPACERW, 2.6 * SPACERH)

        self.port_text_edit = QTextEdit(parent=self)
        self.port_text_edit.resize(190, 30)
        self.port_text_edit.move(5 * SPACERW, 2.6 * SPACERH)
        return

    def setup_save_btn(self):
        self.save_btn = QPushButton(parent=self, text="Save")
        self.save_btn.resize(70, 30)
        self.save_btn.move(6.5 * SPACERW, 4 * SPACERH)
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