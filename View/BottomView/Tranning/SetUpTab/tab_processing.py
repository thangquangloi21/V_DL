from PyQt5.QtWidgets import QFrame, QTabWidget, QWidget, QScrollArea, QLabel, QFormLayout, QCheckBox
from PyQt5.QtCore import QRect
# from View.MainView.main_window import MainWindow


class TabProcess(QScrollArea):
    checkBox: QCheckBox

    def __init__(self, parent, main_window):
        QScrollArea.__init__(self, parent=parent)
        self.main_window: MainWindow = main_window
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.setStyleSheet("""
                          QFrame{
                            background: gray;
                            color: white;
                          }
                          QTextEdit{
                                background-color: rgb(200, 200, 200);
                                border-image: None;
                                font: 14px;
                                color: black;
                          }
                      """)

    def setup_view(self):
        self.setup_process_log()

    def setup_process_log(self):
        content_widget = QWidget()
        self.setWidget(content_widget)
        flay = QFormLayout(content_widget)
        self.setWidgetResizable(True)
        # tesst
        self.t1 = QLabel('Test1')
        i = 100
        while i > 0:
            i -= 1
            self.t1 = QLabel("test " + str(i))
            flay.addRow(self.t1)

    def btn_print_log(self):
        self.checkBox = QCheckBox(self)
        self.checkBox.setGeometry(QRect(0, 475, 81, 20))
        self.checkBox.setObjectName("checkBox")
