from PyQt5.QtWidgets import QLabel, QPushButton, QGridLayout
from PyQt5.QtGui import QCursor, QFont
from PyQt5.QtCore import Qt
from View.MainView.main_window import MainWindow
from View.common_view import VisionPushButton
from View.common_view.vision_frame import VisionFrame


class SetUpTools(VisionFrame):
    set_up_tools_label: QLabel = None
    labeling_btn: QPushButton = None
    auto_create_label_btn: QPushButton = None
    trainning_btn: QPushButton = None
    testing_btn: QPushButton = None
    grid_setupTools: QGridLayout = None

    def __init__(self, parent, main_window):
        VisionFrame.__init__(self, parent=parent)
        self.main_window: MainWindow = main_window
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.setStyleSheet("""
            background: transparent;    
            border-image: url(./Resource/Icon/2. Setuptools.png);
        """)
        self.grid_setupTools = QGridLayout(self)
        self.grid_setupTools.setContentsMargins(30, 10, 20, 0)

    def setup_view(self):
        self.setup_labeling_btn()
        self.setup_auto_create_label_btn()
        self.setup_trainning_btn()
        self.setup_testing_btn()
        self.setup_grid_layout()

    def setup_grid_layout(self):
        # setting  row: int, column: int, rowSpan: int, columnSpan: int
        self.grid_setupTools.addWidget(self.labeling_btn, 0, 0, 1, 1)
        self.grid_setupTools.addWidget(self.auto_create_label_btn, 1, 0, 1, 1)
        self.grid_setupTools.addWidget(self.trainning_btn, 2, 0, 1, 1)
        self.grid_setupTools.addWidget(self.testing_btn, 3, 0, 1, 1)

        # hàng row: int, stretch: int
        self.grid_setupTools.setRowStretch(0, 1)
        self.grid_setupTools.setRowStretch(1, 1)
        self.grid_setupTools.setRowStretch(2, 1)
        self.grid_setupTools.setRowStretch(3, 1)

        # Cột column: int, stretch: int
        self.grid_setupTools.setColumnStretch(0, 1)


    def setup_labeling_btn(self):
        self.labeling_btn = VisionPushButton(parent=self, text="Labeling")
        self.labeling_btn.clicked.connect(self.click_labeling_btn)

    def setup_auto_create_label_btn(self):
        self.auto_create_label_btn = VisionPushButton(parent=self,text="Auto Create Label")
        self.auto_create_label_btn.clicked.connect(self.click_auto_create_label_btn)

    def setup_trainning_btn(self):
        self.trainning_btn = VisionPushButton(parent=self, text="Trainning")
        self.trainning_btn.clicked.connect(self.click_trainning_btn)

    def setup_testing_btn(self):
        self.testing_btn = VisionPushButton(parent=self,text="Testing")
        self.testing_btn.clicked.connect(self.click_testing_btn)

    def click_labeling_btn(self):
        self.main_window.bottom_view.show_frame("Labeling")

    def click_auto_create_label_btn(self):
        self.main_window.bottom_view.show_frame("Auto Create Label")

    def click_trainning_btn(self):
        self.main_window.bottom_view.show_frame("Trainning")

    def click_testing_btn(self):
        self.main_window.bottom_view.show_frame("Testing")
