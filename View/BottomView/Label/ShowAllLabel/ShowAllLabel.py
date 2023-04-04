from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QScrollArea, QWidget, QFormLayout
from PyQt5.QtGui import QIcon, QPixmap
from View.BottomView.Label.ShowAllLabel.object_label import ListObjectLabel
# from View.MainView.main_window import MainWindow

SPACERX = 20
SPACERY = 40


class ShowAllLabel(QMainWindow):
    return_icon: QIcon
    qscroll_list: QScrollArea
    object: ListObjectLabel

    def __init__(self, main_window):
        QMainWindow.__init__(self)
        self.main_window: MainWindow = main_window
        self.row = 500
        self.setup_window()
        self.setup_view()
        self.show()

    def setup_window(self):
        self.setWindowTitle("All Label")
        self.setStyleSheet("""
            QGroupBox {
                background: rgb(100, 100, 100);
                /*background: transparent;*/
                color: white;
                font: 18px;
                font-weight: bold;
                /*background-color:transparent;*/
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
            QPushButton{
                background: rgb(110, 110, 110);
                color: rgb(170,170,170);
                font: 14px;
            }
            QPushButton:hover{
                color: white;
                font-weight: bold;
                font: 17px;                                
                background: orange;
            }
            QPushButton:pressed{
                background: rgb(14, 68, 184);
            }
            QLabel{
                color:black;
                font:16px;
            }
            QComboBox{
                color: white;
                border: 1px solid gray;
                border-radius: 3px;
                padding: 1px 18px 1px 3px;
                min-width: 6em;
            }
            QComboBox:editable {
                background: gray;
            }
            QScrollArea{

            }
        """)
        self.return_icon = QIcon()
        self.return_icon.addPixmap(QPixmap("./Resource/Icon/return2.png"), QIcon.Normal, QIcon.Off)
        self.resize(630, 500)

    def setup_view(self):
        self.setup_label()
        self.setup_list()

    def setup_label(self):
        lbl_name = QLabel(parent=self, text="Name")
        lbl_name.resize(60, 30)
        lbl_name.move(5, 5)

        lbl_img = QLabel(parent=self, text="Image")
        lbl_img.resize(60, 30)
        lbl_img.move(100, 5)
        return

    def setup_list(self):
        self.qscroll_list = QScrollArea(parent=self)
        content_widget = QWidget()
        self.qscroll_list.setWidget(content_widget)
        layout = QFormLayout(content_widget)
        self.qscroll_list.setWidgetResizable(True)

        i = 0
        while i < self.row:
            self.text = QLabel(f"")
            layout.addRow(self.text)
            i += 1

        self.object = ListObjectLabel(parent=self, main_window=self.main_window)
        layout.addChildWidget(self.object)

        self.qscroll_list.resize(620, 450)
        self.qscroll_list.move(5, 1 * SPACERY)
