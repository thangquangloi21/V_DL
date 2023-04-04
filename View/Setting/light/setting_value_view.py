from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QSlider
from View.MainView.main_window import MainWindow
from View.common_view.thanh_tieu_de import ThanhTieuDe

SPACERW = 20
SPACERH = 22


class SettingValueView(QMainWindow):
    thanh_tieu_de: ThanhTieuDe = None
    horizontalSlider: QSlider
    info_lbl: QLabel
    icon: QIcon
    in_val: QPushButton
    de_val: QPushButton
    save_btn: QPushButton

    def __init__(self, main_window):
        QMainWindow.__init__(self)
        self.main_window: MainWindow = main_window

        self.setup_window()
        self.setup_view()
        self.show()

    def setup_window(self):
        self.setFixedSize(350, 180)
        self.setWindowTitle("Light Setting")
        self.setStyleSheet("""
            QMainWindow{
                background: rgb(170, 170, 170);
            }
            QPushButton{
                background: grey;
                font: 15px;
                font-weight: bold;
            }
            QPushButton:hover{
                background-color: light grey;
            }
            QPushButton:pressed{
                background-color: rgb(14, 68, 184);
            }
            QLabel{
                font: 15px;
                bont-weight: bold;
            }
        """)
        self.icon = QIcon()
        self.icon.addPixmap(QPixmap("./Resource/Icon/icon_info.png"), QIcon.Normal, QIcon.Off)
        self.resize(300, 280)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

    def setup_view(self):
        self.setup_thanh_tieu_de()
        self.setup_decrease_val()
        self.setup_info_slider()
        self.setup_slider()
        self.setup_increase_val()
        self.setup_save()

    def setup_thanh_tieu_de(self):
        self.thanh_tieu_de = ThanhTieuDe(parent=self, width=self.width(), height=35, name_window="Light Setting")
        self.thanh_tieu_de.resize(self.width(), 35)
        self.thanh_tieu_de.move(0, 0)
        return

    def setup_slider(self):
        self.horizontalSlider = QSlider(parent=self)
        self.horizontalSlider.setMaximum(255)
        self.horizontalSlider.valueChanged.connect(self.update)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.resize(200, 20)
        self.horizontalSlider.move(3.5 * SPACERW, 4 * SPACERH)

    def setup_info_slider(self):
        self.info_lbl = QLabel(parent=self, text="0")
        self.info_lbl.resize(40, 30)
        self.info_lbl.move(8.5 * SPACERW, 2 * SPACERH)

    def update(self):
        new_value = str(self.horizontalSlider.value())
        self.info_lbl.setText(new_value)

    def setup_increase_val(self):
        self.in_val = QPushButton(parent=self, text=">>>")
        # self.in_val.setIcon(self.icon)
        self.in_val.resize(40, 30)
        self.in_val.move(15 * SPACERW, 3.7 * SPACERH)
        self.in_val.clicked.connect(self.click_increase)
        return

    def setup_decrease_val(self):
        self.de_val = QPushButton(parent=self, text="<<<")
        # self.de_val.setIcon(self.icon)
        self.de_val.resize(40, 30)
        self.de_val.move(5, 3.7 * SPACERH)
        self.de_val.clicked.connect(self.click_decrease)
        return

    def setup_save(self):
        self.save_btn = QPushButton(parent=self, text="Save")
        self.save_btn.resize(70, 30)
        self.save_btn.move(7 * SPACERW, 6 * SPACERH)
        self.save_btn.clicked.connect(self.click_save)
        return

    def click_increase(self):
        self.horizontalSlider.setValue(self.horizontalSlider.value() + 1)

    def click_decrease(self):
        self.horizontalSlider.setValue(self.horizontalSlider.value() - 1)

    def click_save(self):
        self.close()
