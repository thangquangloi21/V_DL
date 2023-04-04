from PyQt5.QtWidgets import QFrame, QCheckBox, QLabel, QComboBox, QPushButton, QWidget, QGroupBox
from PyQt5.QtWidgets import QMainWindow, QLabel, QTextEdit, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox, QLabel, QScrollArea, QHBoxLayout, QVBoxLayout, QWidget, QFormLayout, QFrame, \
    QPushButton
from PyQt5.QtGui import QIcon, QPixmap
# from View.MainView.main_window import MainWindow

SPACERY = 40


class ListObjectLabel(QWidget):
    def __init__(self, parent, main_window):
        QWidget.__init__(self, parent=parent)
        self.main_window: MainWindow = main_window
        self.row = 22
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.resize(590, 450)

    def setup_view(self):
        self.qscroll_list = QScrollArea(parent=self)
        content_widget = QWidget()
        self.qscroll_list.setWidget(content_widget)
        layout = QVBoxLayout(content_widget)
        self.qscroll_list.setWidgetResizable(True)

        i = 0
        while i < self.row:
            self.text = QLabel(f"")
            layout.addWidget(self.text)
            i += 1

        self.obj0 = ObjectLabel(parent=self, main_window=self.main_window)
        self.obj0.resize(590, 200)
        self.obj0.move(0, 0)

        self.obj1 = ObjectLabel(parent=self, main_window=self.main_window)
        self.obj1.move(0, SPACERY)
        self.obj1.resize(590, 200)

        self.obj2 = ObjectLabel(parent=self, main_window=self.main_window)
        self.obj2.move(0, 2 * SPACERY)
        self.obj2.resize(590, 200)

        self.obj3 = ObjectLabel(parent=self, main_window=self.main_window)
        self.obj3.move(0, 3 * SPACERY)
        self.obj3.resize(590, 200)

        self.obj4 = ObjectLabel(parent=self, main_window=self.main_window)
        self.obj4.move(0, 4 * SPACERY)

        self.obj5 = ObjectLabel(parent=self, main_window=self.main_window)
        self.obj5.move(0, 5 * SPACERY)

        self.obj6 = ObjectLabel(parent=self, main_window=self.main_window)
        self.obj6.move(0, 6 * SPACERY)

        self.obj7 = ObjectLabel(parent=self, main_window=self.main_window)
        self.obj7.move(0, 7 * SPACERY)

        self.obj8 = ObjectLabel(parent=self, main_window=self.main_window)
        self.obj8.move(0, 8 * SPACERY)
        return


class ObjectLabel(QFrame):
    qscroll_horizontal: QScrollArea

    def __init__(self, parent, main_window):
        QFrame.__init__(self, parent=parent)
        self.main_window: MainWindow = main_window
        self.col = 22
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.setStyleSheet("""
            QFrame{
                background: red;
                 border-bottom: 15px solid white; /* just a single line */
            }
            QPushButton{
                background: rgb(110, 110, 110);
                color: rgb(220,220,220);
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
            QScrollArea{

            }
        """)

    def setup_view(self):
        self.qscroll_horizontal = QScrollArea(parent=self)
        content_widget = QWidget()
        self.qscroll_horizontal.setWidget(content_widget)
        layout = QHBoxLayout(content_widget)
        self.qscroll_horizontal.setWidgetResizable(True)

        i = 0
        while i < self.col * 10:
            self.img5 = QLabel(parent=self)
            self.img5.setStyleSheet("border-image: url(./Resource/Icon/fgdfg.png);")
            self.img5.resize(30, 30)
            layout.addWidget(self.img5)
            i += 1

        self.qscroll_horizontal.resize(590, 200)
        self.qscroll_horizontal.move(0, 0)
        return
# class ObjectLabel(QLabel):
#     def __init__(self, parent, main_window):
#         QLabel.__init__(self, parent=parent)
#         self.main_window: MainWindow = main_window
#         self.setup_window()
#         self.setup_view()
#
#     def setup_window(self):
#         return
#
#     def setup_view(self):
#         self.lbl = QLabel(parent=self, text="hiii")
#         self.lbl.resize(50, 50)
#         self.lbl.move(0, 0)
