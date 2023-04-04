from PyQt5.QtWidgets import QLabel, QPushButton, QGridLayout
from PyQt5.QtGui import QCursor, QFont
from PyQt5.QtCore import Qt
from View.MainView.main_window import MainWindow
from View.common_view import VisionPushButton
from View.common_view.vision_frame import VisionFrame


class FinishFrame(VisionFrame):
    algorithm_btn: QPushButton = None
    running_btn: QPushButton = None
    finish_label: QLabel = None
    grid_finish: QGridLayout = None

    def __init__(self, parent, main_window):
        VisionFrame.__init__(self, parent=parent)
        self.main_window: MainWindow = main_window
        self.setup_window()
        self.setup_view()

    def setup_window(self):
        self.setStyleSheet("""
            background: transparent;
            border-image: url(./Resource/Icon/3.Finish.png);
        """)
        self.grid_finish = QGridLayout(self)

        self.grid_finish.setContentsMargins(30, 0, 20, 0)

    def setup_view(self):
        self.setup_algorithm_btn()
        self.setup_running_btn()
        self.setup_grid_layout()

    def setup_grid_layout(self):
        # setting  row: int, column: int, rowSpan: int, columnSpan: int
        self.grid_finish.addWidget(self.running_btn,0,0,1,1)
        self.grid_finish.addWidget(self.algorithm_btn,1,0,1,1)

        # hàng  row: int, stretch: int
        self.grid_finish.setRowStretch(0, 1)
        self.grid_finish.setRowStretch(1, 1)

        # Cột column: int, stretch: int
        self.grid_finish.setColumnStretch(0, 1)
    def setup_algorithm_btn(self):
        self.algorithm_btn = VisionPushButton(parent=self,text="Algorithm")
        self.algorithm_btn.clicked.connect(self.click_algorithm)

    def setup_running_btn(self):
        self.running_btn = VisionPushButton(parent=self,text="Running")
        self.running_btn.clicked.connect(self.click_running)

    def click_algorithm(self):
        self.main_window.bottom_view.show_frame("Algorithm")

    def click_running(self):
        self.main_window.bottom_view.show_frame("Running")
