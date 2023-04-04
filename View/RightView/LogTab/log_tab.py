from PyQt5.QtWidgets import QWidget, QScrollArea, QLabel, QFormLayout, QCheckBox, QSizePolicy
from PyQt5.QtCore import QRect


class LogTab(QScrollArea):
    content_widget: QWidget
    checkBox: QCheckBox
    sizePolicy: QSizePolicy

    def __init__(self, parent):
        QScrollArea.__init__(self, parent=parent)
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.setSizePolicy(self.sizePolicy)
        self.setStyleSheet("""
            background: transparent;
            border-image: None;
        """)

    def setup_view(self):
        self.setup_log()
        self.btn_print_log()

    def setup_log(self):
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
