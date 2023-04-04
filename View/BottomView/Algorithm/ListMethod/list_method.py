from PyQt5.QtWidgets import QGroupBox, QLabel, QScrollArea, QWidget, QFormLayout, QGridLayout
from PyQt5.QtGui import QIcon, QPixmap
from View.BottomView.Algorithm.ListMethod.object_method import ListObjectMethod
# from View.MainView.main_window import MainWindow
from PyQt5.QtWidgets import QSizePolicy
from View.common_view.vision_push_button import VisionPushButton
from View.common_view.vision_label import VisionLabel


class ListMethod(QGroupBox):
    return_icon: QIcon = None
    grid_list_method: QGridLayout
    sizePolicy: QSizePolicy

    def __init__(self, parent, main_window):
        QGroupBox.__init__(self, parent=parent)
        self.main_window: MainWindow = main_window
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.setTitle("Select Method")
        self.setStyleSheet("""
            QGroupBox {
                background: rgb(100, 100, 100);
                color: white;
                font: 18px;
                font-weight: bold;
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
        """)
        self.return_icon = QIcon()
        self.return_icon.addPixmap(QPixmap("./Resource/Icon/return2.png"), QIcon.Normal, QIcon.Off)
        self.sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.setSizePolicy(self.sizePolicy)
        self.grid_list_method = QGridLayout(self)

    def setup_view(self):
        self.setup_label()
        self.setup_list()
        self.setup_grid_layout()

    def setup_grid_layout(self):
        self.grid_list_method.addWidget(self.btn_show_origin, 0, 0, 1, 1)
        self.grid_list_method.addWidget(self.lbl_step, 0, 1, 1, 1)
        self.grid_list_method.addWidget(self.lbl_method, 0, 2, 1, 1)
        # self.grid_list_method.addWidget(self.lbl_execute, 0, 3, 1, 1)
        self.grid_list_method.addWidget(self.qscroll_list, 1, 0, 1, 5)

        self.grid_list_method.setColumnStretch(0, 1)
        self.grid_list_method.setColumnStretch(1, 1)
        self.grid_list_method.setColumnStretch(2, 1)
        self.grid_list_method.setColumnStretch(3, 1)
        self.grid_list_method.setColumnStretch(4, 1)

        self.grid_list_method.setRowStretch(0, 1)
        self.grid_list_method.setRowStretch(1, 3)

    lbl_step: VisionLabel
    lbl_method: VisionLabel
    lbl_execute: VisionLabel
    btn_show_origin: VisionPushButton
    qscroll_list: QScrollArea

    def setup_label(self):
        self.lbl_step = VisionLabel( text="Step")

        self.lbl_method = VisionLabel( text="Method")

        # self.lbl_execute = VisionLabel(parent=self, text="Execute")

        self.btn_show_origin = VisionPushButton(parent=self, width=50)
        self.btn_show_origin.setIcon(self.return_icon)
        # self.btn_show_origin.setStyleSheet("background:transparent;")

    object: ListObjectMethod

    def setup_list(self):
        self.qscroll_list = QScrollArea(parent=self)
        content_widget = QWidget()
        self.qscroll_list.setWidget(content_widget)
        layout = QFormLayout(content_widget)
        self.qscroll_list.setWidgetResizable(True)

        i = 0
        while i < 40:
            self.text = QLabel(f"")
            layout.addRow(self.text)
            i += 1

        self.object = ListObjectMethod(parent=self, main_window=self.main_window)
        layout.addChildWidget(self.object)
