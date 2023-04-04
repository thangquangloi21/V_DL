from PyQt5.QtWidgets import QLabel, QGridLayout
from View.common_view.vision_frame import VisionFrame


class Startus(VisionFrame):
    bgr_lbl: QLabel
    bgr_info: QLabel
    result_lbl: QLabel
    result_show: QLabel
    grid_status: QGridLayout

    def __init__(self, parent):
        VisionFrame.__init__(self, parent=parent)
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.setStyleSheet("""
            QFrame{
                border-image: None;
            }
            QLabel{
                color: white;
                font: 14px;
                border-image: None;
            }
        """)
        self.grid_status = QGridLayout(self)
        self.grid_status.setContentsMargins(35, 0, 0, 0)

    def setup_view(self):
        self.setup_bgr_info()
        self.setup_result()
        self.setup_result_info()
        self.setup_grid_layout()

    def setup_grid_layout(self):
        self.grid_status.addWidget(self.bgr_lbl, 0, 0, 1, 1)
        self.grid_status.addWidget(self.bgr_info, 0, 1, 1, 1)
        self.grid_status.addWidget(self.result_lbl, 0, 2, 1, 1)
        self.grid_status.addWidget(self.result_show, 0, 3, 1, 1)

        self.grid_status.setColumnStretch(0, 1)
        self.grid_status.setColumnStretch(1, 1)
        self.grid_status.setColumnStretch(2, 1)
        self.grid_status.setColumnStretch(3, 5)

    def setup_bgr_info(self):
        self.bgr_lbl = QLabel(parent=self, text="(B,G,R)= ")
        self.bgr_info = QLabel(parent=self, text="(0, 0, 0)")

    def setup_result(self):
        self.result_lbl = QLabel(parent=self, text="Result: ")

    def setup_result_info(self):
        self.result_show = QLabel(parent=self, text="info..v...vvvvvvvvvvvvvvv")

