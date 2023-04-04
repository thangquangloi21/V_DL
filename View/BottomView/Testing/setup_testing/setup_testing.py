from PyQt5.QtWidgets import QGroupBox, QGridLayout, QSizePolicy
# from View.MainView.main_window import MainWindow
from View.common_view.vision_push_button import VisionPushButton
from PyQt5.QtCore import QSize


class SetUpTesting(QGroupBox):
    grid_setup_testing: QGridLayout
    open_fordel: VisionPushButton
    select_path: VisionPushButton
    testing_btn: VisionPushButton
    sizePolicy: QSizePolicy

    def __init__(self, parent, main_window):
        QGroupBox.__init__(self, parent=parent)
        self.main_window: MainWindow = main_window
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.setTitle("Testing")
        self.setStyleSheet("""
            QGroupBox {
                background: transparent;
                color: white;
                font: 18px;
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
        """)

        self.setMaximumSize(QSize(300, 16777215))
        self.sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.setSizePolicy(self.sizePolicy)
        self.grid_setup_testing = QGridLayout(self)
        self.grid_setup_testing.setVerticalSpacing(30)
        self.grid_setup_testing.setContentsMargins(10, 50, 10, 0)

    def setup_view(self):
        self.setup_open_btn()
        self.setup_select_weight()
        self.setup_btn_testing()
        self.setup_grid_layout()

    def setup_grid_layout(self):
        self.grid_setup_testing.addWidget(self.open_fordel, 0, 0, 1, 1)
        self.grid_setup_testing.addWidget(self.select_path, 1, 0, 1, 1)
        self.grid_setup_testing.addWidget(self.testing_btn, 2, 0, 1, 1)
        self.grid_setup_testing.setRowStretch(0, 1)
        self.grid_setup_testing.setRowStretch(1, 1)
        self.grid_setup_testing.setRowStretch(2, 1)
        self.grid_setup_testing.setRowStretch(3, 1)

    def setup_open_btn(self):
        self.open_fordel = VisionPushButton(parent=self, text="Select Source Image ")

    def setup_select_weight(self):
        self.select_path = VisionPushButton(parent=self, text="Select Weight Path")

    def setup_btn_testing(self):
        self.testing_btn = VisionPushButton(parent=self, text="Testing")